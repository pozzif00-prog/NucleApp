param([string[]]$Solo)
$ErrorActionPreference = 'Stop'
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

$API = 'https://commons.wikimedia.org/w/api.php'
$UA  = 'NUCLEAPP/1.0 (divulgazione scientifica; contatto: comitato)'
$DIR = Join-Path (Get-Location) 'img'

$IMPIANTI = [ordered]@{
 magnox = @{ nome='Calder Hall'; file='Calder Hall nuclear power station (11823864155).jpg';
   query=@('Calder Hall nuclear power station','Sellafield Calder Hall') }
 rbmk = @{ nome='Chernobyl'; file='Reactor bloc of the Chernobyl Nuclear Power Plant.JPG';
   query=@('Chernobyl Nuclear Power Plant reactor','Chornobyl nuclear power plant') }
 pwr = @{ nome='Sizewell B'; file='Nuclear power station at Sizewell - geograph.org.uk - 210830 retouched.jpg';
   query=@('Sizewell B nuclear power station','Sizewell nuclear power station') }
 bwr = @{ nome='Leibstadt'; file='Leibstadt Kernkraftwerk Leibstadt AG.jpg';
   query=@('Kernkraftwerk Leibstadt','Leibstadt nuclear power plant') }
 candu = @{ nome='Darlington'; file='Darlington Nuclear Generating Station panorama2.jpg';
   query=@('Darlington Nuclear Generating Station','Darlington nuclear Ontario') }
 epr = @{ nome='Olkiluoto 3'; file='Olkiluoto Nuclear Power Plant 2015-07-21 001.jpg';
   query=@('Olkiluoto Nuclear Power Plant','Olkiluoto 3 EPR') }
 ap1000 = @{ nome='Sanmen'; file='Sanmen Nuclear Power Station.jpg';
   query=@('Sanmen Nuclear Power Station','Sanmen nuclear China AP1000') }
 bn800 = @{ nome='Beloyarsk'; file='RIAN archive 895485 Beloyarsk nuclear power plant in Sverdlovsk Region.jpg';
   query=@('Beloyarsk Nuclear Power Plant','Belojarsk nuclear power station') }
 htrpm = @{ nome='Shidaowan (HTR-PM)'; file=$null;
   query=@('Shidao Bay Nuclear Power Plant','HTR-10 Tsinghua reactor','high temperature gas cooled reactor China');
   analogo="Impianto analogo: dell'HTR-PM di Shidaowan non esistono fotografie con licenza libera" }
 onkalo = @{ nome='Onkalo'; file='Olkiluoto Nuclear Power Plant 2015-07-21 001.jpg';
   query=@('Onkalo spent nuclear fuel repository','Olkiluoto island Posiva') }
 wipp = @{ nome='WIPP'; file='WIPP-04.jpeg';
   query=@('Waste Isolation Pilot Plant','WIPP Carlsbad New Mexico') }
 italia = @{ nome='Deposito Nazionale'; file=$null;
   query=@('El Cabril radioactive waste disposal',"Centre de stockage de l'Aube ANDRA",'low level radioactive waste disposal facility');
   analogo="Impianto analogo: il Deposito Nazionale italiano non è ancora stato costruito" }
}

$ESCLUDI = [regex]::new('(logo|map|karte|mapa|diagram|schema|schéma|chart|graph|seal|icon|flag|coat of arms|locator|plan |layout|sign|banner|protest|poster|portrait|\.svg$)','IgnoreCase')
$LIBERE  = [regex]::new('(public domain|cc[ -]?by|cc0|pd-|attribution)','IgnoreCase')
# In modalita' ricerca il titolo DEVE parlare del soggetto giusto, altrimenti
# una parola simile basta a far vincere una foto di tutt'altro (es. "Cabrils").
$TOPICO  = [regex]::new('(nuclear|nucleare|nucléaire|kernkraft|atom|reactor|reattore|réacteur|power (plant|station)|repository|radioactive|radiactivo|radioactif|waste|residuos|déchets|stockage|storage|disposal|\bcabril\b|andra|posiva|onkalo)','IgnoreCase')

function Invoke-Api($params) {
  $params['format'] = 'json'; $params['formatversion'] = '2'
  $qs = ($params.GetEnumerator() | ForEach-Object { "$($_.Key)=$([uri]::EscapeDataString([string]$_.Value))" }) -join '&'
  Invoke-RestMethod -Uri "$API`?$qs" -Headers @{ 'User-Agent' = $UA } -TimeoutSec 60
}

function Pulisci($html) {
  if (-not $html) { return '' }
  $t = [regex]::Replace([string]$html, '<[^>]+>', '')
  $t = $t.Replace('&amp;','&').Replace('&quot;','"').Replace('&#039;',"'")
  $t = ($t -split '\s+' | Where-Object { $_ }) -join ' '
  if ($t.Length -gt 160) { $t = $t.Substring(0,160) }
  return $t
}

function Info-File($titolo) {
  $d = Invoke-Api @{ action='query'; titles="File:$titolo"; prop='imageinfo';
                     iiprop='url|size|extmetadata'; iiurlwidth='1400' }
  $pagine = $d.query.pages
  if (-not $pagine) { return $null }
  $p = @($pagine)[0]
  if ($p.missing) { return $null }
  if (-not $p.imageinfo) { return $null }
  return @($p.imageinfo)[0]
}

function Cerca($query, $n = 12) {
  $d = Invoke-Api @{ action='query'; generator='search'; gsrsearch="filetype:bitmap $query";
                     gsrnamespace='6'; gsrlimit="$n"; prop='imageinfo';
                     iiprop='url|size|extmetadata'; iiurlwidth='1400' }
  $out = New-Object System.Collections.ArrayList
  foreach ($p in @($d.query.pages)) {
    if ($p.imageinfo) { [void]$out.Add([pscustomobject]@{ titolo=[string]$p.title; ii=@($p.imageinfo)[0] }) }
  }
  return ,$out.ToArray()
}

function Valuta([string]$titolo, $ii) {
  if ($ESCLUDI.IsMatch($titolo)) { return -1 }
  if (-not $TOPICO.IsMatch($titolo)) { return -1 }
  $w = [int]$ii.width
  if ($w -lt 700) { return -1 }
  $lic = Pulisci $ii.extmetadata.LicenseShortName.value
  if (-not $LIBERE.IsMatch($lic)) { return -1 }
  $p = [Math]::Min($w, 4000) / 100.0
  $tl = $titolo.ToLower()
  if ($tl.Contains('aerial') -or $tl.Contains('panorama')) { $p += 12 }
  if ([regex]::IsMatch($titolo,'(nuclear|kernkraft|power (plant|station)|repository)','IgnoreCase')) { $p += 18 }
  return $p
}

New-Item -ItemType Directory -Force -Path $DIR | Out-Null
$regPath = Join-Path $DIR 'crediti.json'
$registro = [ordered]@{}
# riparto dal registro esistente, cosi' --solo non cancella gli altri impianti
if (Test-Path $regPath) {
  try {
    $vecchio = (Get-Content $regPath -Raw -Encoding UTF8) | ConvertFrom-Json
    foreach ($p in $vecchio.PSObject.Properties) {
      $registro[$p.Name] = [ordered]@{
        autore = $p.Value.autore; licenza = $p.Value.licenza
        scheda = $p.Value.scheda; analogo = $p.Value.analogo
      }
    }
  } catch { $registro = [ordered]@{} }
}

$ok = 0; $falliti = 0
foreach ($pid_ in $IMPIANTI.Keys) {
  if ($Solo -and ($pid_ -notin $Solo)) { continue }
  $cfg = $IMPIANTI[$pid_]
  Write-Host "`n=== $pid_  ($($cfg.nome))"
  $scelto = $null; $ripiego = $null

  if ($cfg.file) {
    try { $ii = Info-File $cfg.file } catch { $ii = $null }
    if (-not $ii) {
      Write-Host '    file noto non piu disponibile, passo alla ricerca'
    } elseif ([int]$ii.width -lt 700) {
      # anche il file gia' individuato deve reggere la larghezza di visualizzazione:
      # sotto i 700 px la foto esce sgranata, meglio cercarne una piu' grande.
      # Se la ricerca non trova niente di meglio si torna comunque a questo file.
      Write-Host "    file noto troppo piccolo ($($ii.width) px), cerco di meglio"
      $ripiego = @($cfg.file, $ii)
    } else {
      $scelto = @($cfg.file, $ii); Write-Host '    file noto trovato'
    }
  }

  if (-not $scelto) {
    foreach ($q in $cfg.query) {
      try { $cands = Cerca $q } catch { $cands = @() }
      $scored = New-Object System.Collections.ArrayList
      foreach ($c in $cands) {
        $s = Valuta $c.titolo $c.ii
        if ($s -gt 0) { [void]$scored.Add([pscustomobject]@{ punti=[double]$s; titolo=$c.titolo; ii=$c.ii }) }
      }
      if ($scored.Count) {
        $best = ($scored | Sort-Object punti -Descending)[0]
        $scelto = @(($best.titolo -replace '^File:',''), $best.ii)
        Write-Host "    trovato cercando <<$q>>"
        break
      }
    }
  }

  if (-not $scelto -and $ripiego) {
    $scelto = $ripiego
    Write-Host '    niente di meglio: tengo il file noto'
  }
  if (-not $scelto) { Write-Host '    NESSUNA immagine libera trovata'; $falliti++; continue }

  $titolo = $scelto[0]; $ii = $scelto[1]
  $autore = Pulisci $ii.extmetadata.Artist.value;            if (-not $autore) { $autore = 'autore non indicato' }
  $lic    = Pulisci $ii.extmetadata.LicenseShortName.value;  if (-not $lic)    { $lic = 'licenza da verificare' }
  Write-Host "    $titolo"
  Write-Host "    $autore - $lic"

  # Special:FilePath produce sempre un JPEG (converte anche TIFF) e non viene
  # limitato come l'URL diretto delle miniature su upload.wikimedia.org
  $url = 'https://commons.wikimedia.org/wiki/Special:FilePath/' +
         [uri]::EscapeDataString($titolo.Replace(' ','_')) + '?width=1400'
  $dest = Join-Path $DIR "$pid_.jpg"
  $scaricato = $false
  foreach ($tentativo in 1..6) {
    try {
      Invoke-WebRequest -Uri $url -Headers @{ 'User-Agent' = $UA } -OutFile $dest -TimeoutSec 120
      $scaricato = $true; break
    } catch {
      $msg = $_.Exception.Message
      if ($tentativo -eq 6) { Write-Host "    ERRORE nel download: $msg"; break }
      $attesa = 5 * $tentativo
      Write-Host "    tentativo $tentativo non riuscito, riprovo tra $attesa s"
      Start-Sleep -Seconds $attesa
    }
  }
  if (-not $scaricato) { $falliti++; continue }
  $kb = [int]((Get-Item $dest).Length / 1024)
  Write-Host "    salvato in $dest  ($kb KB)"
  Start-Sleep -Seconds 3

  $registro[$pid_] = [ordered]@{
    autore  = $autore
    licenza = $lic
    scheda  = 'https://commons.wikimedia.org/wiki/File:' + [uri]::EscapeDataString($titolo.Replace(' ','_')).Replace('%2F','/')
    analogo = if ($cfg.analogo) { $cfg.analogo } else { '' }
  }
  $ok++
}

$json = $registro | ConvertTo-Json -Depth 5
[IO.File]::WriteAllText($regPath, $json, (New-Object Text.UTF8Encoding $false))
[IO.File]::WriteAllText((Join-Path $DIR 'crediti.js'), "window.CREDITI_LOCALI = $json;`n", (New-Object Text.UTF8Encoding $false))
Write-Host "`n---------------------------------------------"
Write-Host "immagini pronte: $ok    non riuscite: $falliti"
