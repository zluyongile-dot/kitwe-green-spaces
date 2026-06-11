$pages = 'about-green-spaces.html','bibliography.html','documentation.html','feedback.html','report-generator.html','advanced-stats.html','environmental-monitoring-new.html'

$cssLink = '    <link rel="stylesheet" href="page-dark.css">'
$faviconLink = '    <link rel="icon" type="image/svg+xml" href="favicon.svg">'
$googleFonts = '    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Outfit:wght@600;700;800&display=swap" rel="stylesheet">'

$navbarScript = @'

    <script>
    (function(){
        var page = window.location.pathname.split('/').pop();
        function lnk(href,icon,label){ var a=document.createElement('a');a.href=href;if(page===href)a.className='active';a.innerHTML='<i class="fas fa-'+icon+'"></i> '+label;return a; }
        var bar = document.createElement('div');
        bar.id = 'kgs-topbar';
        var brand=document.createElement('a');brand.className='brand';brand.href='home.html';
        brand.innerHTML='<span class="dot"><i class="fas fa-tree"></i></span>Kitwe Green Spaces';
        var links=document.createElement('div');links.className='links';
        links.appendChild(lnk('index.html','map','Map'));
        links.appendChild(lnk('simpledashboard.html','chart-bar','Dashboard'));
        links.appendChild(lnk('3d-view.html','satellite-dish','Satellite Tour'));
        links.appendChild(lnk('about-green-spaces.html','info-circle','About'));
        var cta=document.createElement('a');cta.href='index.html';cta.className='cta';cta.innerHTML='<i class="fas fa-map"></i> Launch Map';
        links.appendChild(cta);
        bar.appendChild(brand);bar.appendChild(links);
        document.body.insertBefore(bar,document.body.firstChild);
    })();
    </script>
'@

foreach ($page in $pages) {
    $path = "c:\Users\I LOVE THIS PC\Desktop\kitwe-green-spaces-main\frontend\$page"
    if (Test-Path $path) {
        $content = Get-Content $path -Raw -Encoding UTF8
        if ($content -match 'page-dark\.css') {
            Write-Host "Already done: $page"
            continue
        }
        $inject = "$cssLink`n$faviconLink`n$googleFonts`n</head>"
        $content = $content -replace '</head>', $inject
        $content = $content -replace '</body>', "$navbarScript`n</body>"
        Set-Content $path $content -Encoding UTF8
        Write-Host "Updated: $page"
    } else {
        Write-Host "NOT FOUND: $page"
    }
}
Write-Host "All done."
