# PARSING HTML COM BEAUTIFUL SOUP 

<h3> IMPORTANDO O BEAUTIFUL SOUP E URLLIB </H3>

        >>> from bs4 import BeautifulSoup
        >>> import urllib

<h3> PEGANDO O HTML </h3>

        >>> html = urllib.urlopen('http://www.silviosantos.com.br')
        >>> html
        <addinfourl at 139819276339248 whose fp = <socket._fileobject object at 0x7f2a36d5e150>>
        >>> html.code
        200

<h3> CHAMANDO O PARSER </h3>

        >>> bt = BeautifulSoup(html.read(), "lxml")

<h3> TAGS </h3> 

        >>> bt = BeautifulSoup(html.read(), "lxml")
        >>> bt.title
        <title>Silvio Santos</title>

        #imprimir o titulo como uma string
        >>> bt.title.string
        u'Silvio Santos'
 
        #imprimir o proprio nome da tag
        >>> bt.title.name
        'title'

        #meta tag
        >>> bt.meta
        <meta charset="unicode-escape"/>

        # proxima tag
        >>> bt.meta.next
        u'\n'
        >>> bt.meta.next.next
        <meta content="Silvio Santos" name="keywords"/>
        
        #buscando todas as meta tags com a funcao find_all
        >>> allMetaTags = bt.find_all('meta')
        >>> allMetaTags
        [<meta charset="unicode-escape"/>, <meta content="Silvio Santos" name="keywords"/>, <meta content="Silvio Santos" name="news_keywords"/>, <meta content="Site do apresentador Silvio Santos, com biografia, curiosidades, v\xeddeos e muito mais" name="description"/>, <meta content="1 hour" name="revisit-after"/>, <meta content="noodp" name="googlebot"/>, <meta content="index, follow" name="robots"/>, <meta content="http://www.sbt.com.br/silviosantos/" property="og:url"/>, <meta content="website" property="og:type"/>, <meta content="pt_BR" property="og:locale"/>, <meta content="Silvio Santos" property="og:title"/>, <meta content="http://www.facebook.com/sbtonline" property="article:author"/>, <meta content="http://www.sbt.com.br/images/logos_wide/178_480x360.jpg" property="og:image"/>, <meta content="Site do apresentador Silvio Santos, com biografia, curiosidades, v\xeddeos e muito mais" property="og:description"/>, <meta content="SBT - Sistema Brasileiro de Televis\xe3o" property="og:site_name"/>, <meta content="{698199030202864}" property="fb:admins"/>, <meta content="132520803451684" property="fb:pages"/>, <meta content="0biRI59l3UnkfcsqD8GH6QVXizM" name="alexaVerifyID"/>, <meta content="width=1260" name="viewport"/>]

<h5> Agora trabalhando um pouco mais essa resposta:  </h5> 

        >>> for i in range (len(allMetaTags)):
        ...     print allMetaTags[i]
        ... 
        <meta charset="utf-8"/>
        <meta content="Silvio Santos" name="keywords"/>
        <meta content="Silvio Santos" name="news_keywords"/>
        <meta content="Site do apresentador Silvio Santos, com biografia, curiosidades, vídeos e muito mais" name="description"/>
        <meta content="1 hour" name="revisit-after"/>
        <meta content="noodp" name="googlebot"/>
        <meta content="index, follow" name="robots"/>
        <meta content="http://www.sbt.com.br/silviosantos/" property="og:url"/>
        <meta content="website" property="og:type"/>
        <meta content="pt_BR" property="og:locale"/>
        <meta content="Silvio Santos" property="og:title"/>
        <meta content="http://www.facebook.com/sbtonline" property="article:author"/>
        <meta content="http://www.sbt.com.br/images/logos_wide/178_480x360.jpg" property="og:image"/>
        <meta content="Site do apresentador Silvio Santos, com biografia, curiosidades, vídeos e muito mais" property="og:description"/>
        <meta content="SBT - Sistema Brasileiro de Televisão" property="og:site_name"/>
        <meta content="{698199030202864}" property="fb:admins"/>
        <meta content="132520803451684" property="fb:pages"/>
        <meta content="0biRI59l3UnkfcsqD8GH6QVXizM" name="alexaVerifyID"/>
        <meta content="width=1260" name="viewport"/>

<h5> Podemos tambem acessar os atributos como chave/valor de dicionario: </h5> 

        >>> allMetaTags[0]['charset']
        u'iso-8859-1'
        >>> allMetaTags[1]['content']
        'Silvio Santos'
<h3> ENCONTRANDO TODOS OS LINKS DENTRO DE UM DOCUMENTO HTML </H3>

        >>> alllinks
        >>> allLinks = bt.find_all('a')
        >>> len(allLinks)
        42
        >>> allLinks
        [<a href="http://www.sbt.com.br/home/" title="SBT - Sistema Brasileiro de Televis\xe3o">\n<img alt="SBT - Sistema Brasileiro de Televis\xe3o" src="/images/campanha2015/top/logo.png" title="SBT - Sistema Brasileiro de Televis\xe3o"/>\n</a>, <a class="hassubmenu" href="javascript:void(0);" rel="SubmenuProgramas" style="margin: 0px 10px;" title="Programas">Programas</a>, <a href="/programacao/" style="margin: 0px 10px;" title="Programa\xe7\xe3o">Programa\xe7\xe3o</a>, <a href="/sbtvideos/" style="margin: 0px 10px;" title="SBT V\xeddeos">SBT V\xeddeos</a>, <a href="/inscricoes/" style="margin: 0px 10px;" title="Inscri\xe7\xf5es">Inscri\xe7\xf5es</a>, <a href="/jornalismo/" style="margin: 0px 10px;" title="Jornalismo">Jornalismo</a>, <a class="hassubmenu" href="javascript:void(0);" rel="SubmenuNaweb" style="margin: 0px 10px;" title="Na Web">Na Web</a>, <a class="topAoVivo" href="http://www.sbt.com.br/aovivo/">SBT Ao Vivo</a>, <a href="javascript:void(0);">Linha de Shows</a>, <a href="javascript:void(0);">Novelas</a>, <a href="javascript:void(0);">Infantil</a>, <a href="javascript:void(0);">Filmes e S\xe9ries</a>, <a href="javascript:void(0);">Jornalismo</a>, <a href="javascript:void(0);">Eventos</a>, <a class="W100PERC H40 BOX" href="/silviosantos/trajetoria" title="A Trajet\xf3ria">A Trajet\xf3ria</a>, <a class="W100PERC H40 BOX" href="/silviosantos/oanimador" title="O Animador">O Animador</a>, <a class="W100PERC H40 BOX" href="/silviosantos/curiosidades" title="Curiosidades">Curiosidades</a>, <a class="W100PERC H40 BOX" href="/silviosantos/depoimentos" title="Depoimentos">Depoimentos</a>, <a class="W100PERC H40 BOX" href="/silviosantos/fotos" title="Fotos">Fotos</a>, <a class="BOX W100PERC H100PERC NOTEXT" href="/silviosantos/">Silvio Santos</a>, <a class="W100PERC H40 BOX" href="/silviosantos/trajetoria" title="A Trajet\xf3ria">A Trajet\xf3ria</a>, <a class="W100PERC H40 BOX" href="/silviosantos/oanimador" title="O Animador">O Animador</a>, <a class="W100PERC H40 BOX" href="/silviosantos/curiosidades" title="Curiosidades">Curiosidades</a>, <a class="W100PERC H40 BOX" href="/silviosantos/depoimentos" title="Depoimentos">Depoimentos</a>, <a class="W100PERC H40 BOX" href="/silviosantos/fotos" title="Fotos">Fotos</a>, <a href="/silviosantos/trajetoria/">Confira sua <span>Trajet\xf3ria</span> de vida.</a>, <a href="/silviosantos/oanimador/">Saiba mais</a>, <a href="/silviosantos/curiosidades/">Confira</a>, <a href="/silviosantos/fotos/">Ver Fotos</a>, <a href="http://www.sbt.com.br/institucional/" title="Quem Somos">Institucional</a>, <a href="http://www.sbt.com.br/app/" title="Baixe o APP SBT">Baixe o APP SBT</a>, <a href="http://www.sbt.com.br/tvdigital/sinal/" title="Sinal Digital">Sinal Digital</a>, <a href="/institucional/" title="Quem Somos">Quem Somos</a>, <a href="http://www.sbt.com.br/sbtdobem/" title="Responsabilidade Social">Responsabilidade Social</a>, <a href="http://www.sbt.com.br/internationalsales/" title="International Sales">International Sales</a>, <a href="http://www.sbt.com.br/institucional/ondeestamos/" title="Quem Somos">Onde Estamos</a>, <a href="http://www.sbt.com.br/pesquisadesinal/" title="Pesquisa de Sinal">Pesquisa de Sinal</a>, <a href="http://www.vagas.com.br/sbt" target="_blank" title="Trabalhe no SBT">Trabalhe no SBT</a>, <a href="http://sbtsaladeimprensa.com.br" target="_blank" title="Sala de Imprensa">Sala de Imprensa</a>, <a href="http://www.telesena.com.br/" target="_blank" title="Lideran\xe7a Capitaliza\xe7\xe3o">Lideran\xe7a Capitaliza\xe7\xe3o</a>, <a href="http://www.jequiti.com.br" target="_blank" title="Jequiti">Jequiti</a>, <a href="http://www.sofitel.com/gb/hotel-6383-sofitel-jequitimar-guaruja/index.shtml" target="_blank" title="Hotel Jequitimar">Hotel Jequitimar</a>]

<h5> Organizando um pouco mais as coisas </h5>

    for i in range(len(allLinks)):
    ...     print allLinks[i]
    ... 
    <a href="http://www.sbt.com.br/home/" title="SBT - Sistema Brasileiro de Televisão">
    <img alt="SBT - Sistema Brasileiro de Televisão" src="/images/campanha2015/top/logo.png" title="SBT - Sistema Brasileiro de Televisão"/ </a>    
    <a class="hassubmenu" href="javascript:void(0);" rel="SubmenuProgramas" style="margin: 0px 10px;" title="Programas">Programas</a>
    <a href="/programacao/" style="margin: 0px 10px;" title="Programação">Programação</a>
    <a href="/sbtvideos/" style="margin: 0px 10px;" title="SBT Vídeos">SBT Vídeos</a>
    <a href="/inscricoes/" style="margin: 0px 10px;" title="Inscrições">Inscrições</a>
    <a href="/jornalismo/" style="margin: 0px 10px;" title="Jornalismo">Jornalismo</a>
    <a class="hassubmenu" href="javascript:void(0);" rel="SubmenuNaweb" style="margin: 0px 10px;" title="Na Web">Na Web</a>
    <a class="topAoVivo" href="http://www.sbt.com.br/aovivo/">SBT Ao Vivo</a>
    <a href="javascript:void(0);">Linha de Shows</a>
    <a href="javascript:void(0);">Novelas</a>
    <a href="javascript:void(0);">Infantil</a>
    <a href="javascript:void(0);">Filmes e Séries</a>
    <a href="javascript:void(0);">Jornalismo</a>
    <a href="javascript:void(0);">Eventos</a>
    <a class="W100PERC H40 BOX" href="/silviosantos/trajetoria" title="A Trajetória">A Trajetória</a>
    <a class="W100PERC H40 BOX" href="/silviosantos/oanimador" title="O Animador">O Animador</a>
    <a class="W100PERC H40 BOX" href="/silviosantos/curiosidades" title="Curiosidades">Curiosidades</a>
    <a class="W100PERC H40 BOX" href="/silviosantos/depoimentos" title="Depoimentos">Depoimentos</a>
    <a class="W100PERC H40 BOX" href="/silviosantos/fotos" title="Fotos">Fotos</a>
    <a class="BOX W100PERC H100PERC NOTEXT" href="/silviosantos/">Silvio Santos</a>
    <a class="W100PERC H40 BOX" href="/silviosantos/trajetoria" title="A Trajetória">A Trajetória</a>
    <a class="W100PERC H40 BOX" href="/silviosantos/oanimador" title="O Animador">O Animador</a>
    <a class="W100PERC H40 BOX" href="/silviosantos/curiosidades" title="Curiosidades">Curiosidades</a>
    <a class="W100PERC H40 BOX" href="/silviosantos/depoimentos" title="Depoimentos">Depoimentos</a>
    <a class="W100PERC H40 BOX" href="/silviosantos/fotos" title="Fotos">Fotos</a>
    <a href="/silviosantos/trajetoria/">Confira sua <span>Trajetória</span> de vida.</a>
    <a href="/silviosantos/oanimador/">Saiba mais</a>
    <a href="/silviosantos/curiosidades/">Confira</a>
    <a href="/silviosantos/fotos/">Ver Fotos</a>
    <a href="http://www.sbt.com.br/institucional/" title="Quem Somos">Institucional</a>
    <a href="http://www.sbt.com.br/app/" title="Baixe o APP SBT">Baixe o APP SBT</a>
    <a href="http://www.sbt.com.br/tvdigital/sinal/" title="Sinal Digital">Sinal Digital</a>
    <a href="/institucional/" title="Quem Somos">Quem Somos</a>
    <a href="http://www.sbt.com.br/sbtdobem/" title="Responsabilidade Social">Responsabilidade Social</a>
    <a href="http://www.sbt.com.br/internationalsales/" title="International Sales">International Sales</a>
    <a href="http://www.sbt.com.br/institucional/ondeestamos/" title="Quem Somos">Onde Estamos</a>
    <a href="http://www.sbt.com.br/pesquisadesinal/" title="Pesquisa de Sinal">Pesquisa de Sinal</a>
    <a href="http://www.vagas.com.br/sbt" target="_blank" title="Trabalhe no SBT">Trabalhe no SBT</a>
    <a href="http://sbtsaladeimprensa.com.br" target="_blank" title="Sala de Imprensa">Sala de Imprensa</a>
    <a href="http://www.telesena.com.br/" target="_blank" title="Liderança Capitalização">Liderança Capitalização</a>
    <a href="http://www.jequiti.com.br" target="_blank" title="Jequiti">Jequiti</a>
    <a href="http://www.sofitel.com/gb/hotel-6383-sofitel-jequitimar-guaruja/index.shtml" target="_blank" title="Hotel Jequitimar">Hotel Jequitimar</a>

<h5> Ver a string de cada item: </h5> 

    >>> allLinks[1].string
    u'Programas'
    >>> allLinks[2].string
    u'Programa\xe7\xe3o'
    >>> allLinks[3].string
    u'SBT V\xeddeos'

<h5> Dando uma olhada no HREF: </h5>

        >>> allLinks[0]['href']
        'http://www.sbt.com.br/home/'

<h5> Imprimindo todos os links: </h5>

        >>> for i in range(len(allLinks)):
        ...     print allLinks[i]['href']
        ... 
        http://www.sbt.com.br/home/
        javascript:void(0);
        /programacao/
        /sbtvideos/
        /inscricoes/
        /jornalismo/
        javascript:void(0);
        http://www.sbt.com.br/aovivo/
        javascript:void(0);
        javascript:void(0);
        javascript:void(0);
        javascript:void(0);
        javascript:void(0);
        javascript:void(0);
        /silviosantos/trajetoria
        /silviosantos/oanimador
        /silviosantos/curiosidades
        /silviosantos/depoimentos
        /silviosantos/fotos
        /silviosantos/
        /silviosantos/trajetoria
        /silviosantos/oanimador
        /silviosantos/curiosidades
        /silviosantos/depoimentos
        /silviosantos/fotos
        /silviosantos/trajetoria/
        /silviosantos/oanimador/
        /silviosantos/curiosidades/
        /silviosantos/fotos/
        http://www.sbt.com.br/institucional/
        http://www.sbt.com.br/app/
        http://www.sbt.com.br/tvdigital/sinal/
        /institucional/
        http://www.sbt.com.br/sbtdobem/
        http://www.sbt.com.br/internationalsales/
   
<h3> OBTENDO TODO O TEXTO CRU DO DOCUMENTO </h3> 

        >>> bt.get_text()
        u'\n\nSilvio Santos\n\n\n\n\n\n\n\n\n\n\n\n\n\nvar _sf_startpt=(new Date()).getTime()\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\r\n\t\tvar googletag = googletag || {};\r\n\t\tgoogletag.cmd = googletag.cmd || [];\r\n\t\t(function(){\r\n\t\t\tvar gads = document.createElement(\'script\');\r\n\t\t\tgads.async = true;\r\n\t\t\tgads.type = \'text/javascript\';\r\n\t\t\tvar useSSL = \'https:\' == document.location.protocol;\r\n\t\t\tgads.src = (useSSL ? \'https:\' : \'http:\') + \'//www.googletagservices.com/tag/js/gpt.js\';\r\n\t\t\tvar node = document.getElementsByTagName(\'script\')[0];\r\n\t\t\tnode.parentNode.insertBefore(gads, node);\r\n\t\t})();\r\n\t\n\r\n\t\tgoogletag.cmd.push(function(){\r\n\t\t\tgoogletag.defineSlot(\'/1011235/300x250_Novelas_cuidadocomoanjo_Sbt_Latera_2\t\', [300, 250], \'banner300x250\').addService(googletag.pubads());\r\ngoogletag.defineSlot(\'/1011235/468x60_Novelas_cuidadocomoanjo\', [468, 60], \'banner468x60_Topo\').addService(googletag.pubads());\r\ngoogletag.defineSlot(\'/1011235/728x90_Novelas_cuidadocomoanjo_Sbt_Rodape\', [728, 90], \'banner728x90_Rodape\').addService(googletag.pubads());\r\ngoogletag.defineSlot(\'/1011235/\', [200, 90], \'banner205x105\').addService(googletag.pubads());\r\n\r\n\t\t\tgoogletag.defineSlot(\'/1011235/970x250_WebDigital_Billbord\', [970, 250], \'div-gpt-ad-1473989071096-0\').addService(googletag.pubads());\r\n\t\t\t\r\n\t\t\tgoogletag.pubads().enableSingleRequest();\r\n\t\t\tgoogletag.pubads().collapseEmptyDivs(true);\r\n\t\t\tgoogletag.enableServices();\r\n\t\t});\r\n\t\t\r\n\t\t$(document).ready(function(){\r\n\t\t\t/* ----- dispatch event ------ */\r\n\t\t\tfunction verifyHeight(){\r\n\t\t\t\tvar h = $("#bannerFloater").height();\r\n\t\t\t\t$("body").trigger( "carregoubillboard", h );\r\n\t\t\t}\r\n\t\t\tsetTimeout(function(){ verifyHeight() }, 1000);\r\n\t\t\t\r\n\t\t\t$("body").on(\'carregoubillboard\', function(e, var1){\r\n\t\t\t\tvar alturaTopoSBT \t\t= $("#ContentTopSBT").height();\r\n\t\t\t\tvar alturaTopoHotsite \t= $("#ContentMaster #Topo").height();\r\n\t\t\t\tvar vHeightBG\t\t= ( (\'\'+$("body").attr("id")).toLowerCase() == "pgaovivo" )?(alturaTopoSBT + var1) +\'px\': (alturaTopoSBT + alturaTopoHotsite + var1 +\'px\');\r\n\t\t\t\t$(".advancedOptions div div").css("top", vHeightBG);\r\n\t\t\t\t$("#bannerFloater").css("border-bottom-width","3px");\r\n\t\t\t});\r\n\t\t});\r\n\t\t\r\n\t\t\r\n\t\n\n\n\n\n\n\n\n\n\n\n\r\n\t\t$(function(){\r\n\t\t\t\r\n\t\t\t\r\n\t\t\t\t$(window).scroll(function(){\r\n\t\t\t\t\tif ( $(window).scrollTop() > ($(\'#ContentMenu\').offset().top) ){\r\n\t\t\t\t\t\t$(".overMenu").fadeIn(300);\r\n\t\t\t\t\t\treturn false;\r\n\t\t\t\t\t}else{\r\n\t\t\t\t\t\t$(".overMenu").fadeOut(300);\r\n\t\t\t\t\t}\r\n\t\t\t\t});\r\n\t\t\t\r\n\t\t\t\r\n\t\t});\r\n\t\n\n\n\n\n\n(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({\'gtm.start\':new Date().getTime(),event:\'gtm.js\'});var f=d.getElementsByTagName(s)[0], j=d.createElement(s),dl=l!=\'dataLayer\'?\'&l=\'+l:\'\';j.async=true;j.src=\'//www.googletagmanager.com/gtm.js?id=\'+i+dl;f.parentNode.insertBefore(j,f);\r\n})(window,document,\'script\',\'dataLayer\',\'GTM-52W4BR\');\n\n\n\n\n\n\n\n\n\nProgramas\nPrograma\xe7\xe3o\nSBT V\xeddeos\nInscri\xe7\xf5es\nJornalismo\nNa Web\n\n\nSBT Ao Vivo\n\n\n\n\n\n\n\n\n\n\n\n\n\nLinha de Shows\nNovelas\nInfantil\nFilmes e S\xe9ries\nJornalismo\nEventos\n\n\n\n\n\n\n\n\n\n\n\n\n\ngoogletag.cmd.push(function() { googletag.display(\'div-gpt-ad-1473989071096-0\'); });\n\n\n\n\n\n\n\n\nA Trajet\xf3ria\nO Animador\nCuriosidades\nDepoimentos\nFotos\n\n\n\n\n\nSilvio Santos\n\n\n\nA Trajet\xf3ria\nO Animador\nCuriosidades\nDepoimentos\nFotos\n\n\n\n\n\n\n\n\n\n"Em 2015, Silvio Santos completou 85 anos. Com uma carreira sempre em ascens\xe3o, o apresentador continua \xe0 frente do Programa Silvio Santos e do Roda a Roda Jequiti! "\nConfira sua Trajet\xf3ria de vida.\n\n\nSaiba tudo sobre a carreira de Silvio Santos e relembre os programas comandados por ele.\nSaiba mais\n\n\nDescobrimos com pessoas pr\xf3ximas ao apresentador informa\xe7\xf5es exclusivas sobre o maior astro da televis\xe3o brasileira!\nConfira\n\n\nVeja fotos que marcam a vida e a carreira de Silvio Santos!\nVer Fotos\n\n\n\r\n\t\t$(function(){\r\n\t\t\tSiteObj.getVideoHome(\'.embedVideoSilvioSantos\');\r\n\t\t});\r\n\t\n\n\n\n\n\n\n\nSBT Copyright \xa9 2018 - Sistema Brasileiro de Televis\xe3o (11)3236 0111\n\n\n\nSOBRE O SBT\n\nInstitucional\nBaixe o APP SBT\nSinal Digital\nQuem Somos\nResponsabilidade Social\nInternational Sales\nOnde Estamos\nPesquisa de Sinal\nTrabalhe no SBT\nSala de Imprensa\n\n\n\nGRUPO SILVIO SANTOS\n\nLideran\xe7a Capitaliza\xe7\xe3o\nJequiti\nHotel Jequitimar\n\n\n\n\n\n\n\n\n\n\n\r\n\tfunction returnRegionalLabel(reg){\r\n\t\treturn \'label\'+reg;\r\n\t}\r\n\t$(document).ready(function(){\r\n\t\t//$(this).sbttrack();\r\n\t\tif(SBTAPI){\r\n\t\t\tSBTAPI.getProgram(\'gender\',{\r\n\t\t\tid:178,\r\n\t\t\tlimit:1\r\n\t\t},function(json){\r\n\t\t\tif( json.programs ){\r\n\t\t\t\tvar txtGenero;\r\n\t\t\t\t$.each(json.programs, function(i,item){\t\t\t\t\t\r\n\t\t\t\t\ttxtGenero = item.gender;\r\n\t\t\t\t\t$(\'.generoFooter\').append(\'| &nbsp;&nbsp;\'+txtGenero);\r\n\t\t\t\t});\t\t\t\t\r\n\t\t\t}\r\n\t\t},{v:\'2.0.1\',k:(((document.domain).indexOf(\'sbt.com.br\') >= 0)?\'AE8C984EECBA4F7F835C585D5CB6AB4B\':\'50E675EF86524FA9AE3344C26AB7F645\'),u:\'http://api.sbt.com.br\'});\r\n\t\t\t\r\n\t\t\tSBTAPI.getProgramSchedule(\'id,title,link,startDate,thumbnail\',{limit:10},function(data){\r\n\t\t\t\r\n\t\t\t\tif(data.programschedule){\r\n\t\t\t\t\tvar hora;\r\n\t\t\t\t\tvar urlAtual = "";\r\n\t\t\t\t\tif(data.programschedule.length > 0){\r\n\t\t\t\t\t\t$("#ContentProgramScheduler .Middle").append(\'<div class="label \'+ returnRegionalLabel(\'\') +\'" />\');\r\n\t\t\t\t\t\t$("#ContentProgramScheduler .Middle").append("<ul />");\r\n\t\t\t\t\t\tvar flag = "";\r\n\t\t\t\t\t\tvar width = 0;\r\n\t\t\t\t\t\t$.each(data.programschedule,function(indexItem,item){\r\n\t\t\t\t\t\t\thora = item.startdate.substr(11,5);\r\n\r\n\t\t\t\t\t\t\tif(indexItem==0){\r\n\t\t\t\t\t\t\t\tflag=\'Agora\';\r\n\t\t\t\t\t\t\t\titem.link = "http://www.sbt.com.br/aovivo/";\r\n\t\t\t\t\t\t\t}else if(indexItem==1){\r\n\t\t\t\t\t\t\t\tflag=\'A seguir\'\r\n\t\t\t\t\t\t\t}else{\r\n\t\t\t\t\t\t\t\tflag=\'\'\r\n\t\t\t\t\t\t\t}\r\n\r\n\t\t\t\t\t\t\t$("#ContentProgramScheduler .Middle ul").append(\'<li><a href="\'+ item.link +\'" title="\'+ item.title +\'"><span class="flag">\'+ flag +\'</span><span class="hour">\'+ hora +\'</span><h5>\'+ item.title +\'</h5></a></li>\');\r\n\t\t\t\t\t\t\twidth = $("#ContentProgramScheduler .Middle ul").width();\r\n\t\t\t\t\t\t\tif(width > 870){\r\n\t\t\t\t\t\t\t\t$("#ContentProgramScheduler .Middle ul li:nth-child("+(indexItem+1)+")").css({"display":"none"});\r\n\t\t\t\t\t\t\t\t$("#ContentProgramScheduler .Middle").append(\'<a href="/programacao/" class="gradeCompleta" title="Grade completa">Grade completa</a><div class="contentSocialFooter"><a href="http://www.sbt.com.br/pesquisadesinal" class="icon-pesquisa-sinal"></a><a href="https://www.youtube.com/SBTonline" target="_blank" class="ico ico-youtube"></a><a href="https://www.facebook.com/SBTonline" target="_blank" class="ico ico-facebook"></a><a href="https://twitter.com/SBTonline" target="_blank" class="ico ico-twitter"></a><a href="http://www.instagram.com/sbtonline/" target="_blank" class="ico ico-instagram"></a><a href="https://plus.google.com/+SBTOnline" target="_blank" class="ico ico-google"></a></div>\');\r\n\t\t\t\t\t\t\t\treturn false;\r\n\t\t\t\t\t\t\t}\r\n\r\n\t\t\t\t\t\t\tif(flag==\'Agora\'){\r\n\t\t\t\t\t\t\t\t$("#ContentProgramScheduler li:first-child span").addClass("aovivo");\t\r\n\t\t\t\t\t\t\t}\r\n\t\t\t\t\t\t});\r\n\t\t\t\t\t}\r\n\t\t\t\t}\r\n\t\t\t},{v:\'homesbt\',k:(((document.domain).indexOf(\'sbt.com.br\') >= 0)?\'AE8C984EECBA4F7F835C585D5CB6AB4B\':\'50E675EF86524FA9AE3344C26AB7F645\'),u:\'http://api.sbt.com.br\'});\r\n\t\t}\r\n\r\n\t\tif($.browser.msie){\r\n\t\t\tif(parseInt($.browser.version) < 8){\r\n\t\t\t\tvar urlIEException = "/ie.html?TB_iframe=false&height=199&width=399&modal=true";\r\n\t\t\t\ttb_show("IE", urlIEException);\r\n\t\t\t\t$("#TB_window").css({"background":"#525252","overflow":"hidden"});\r\n\t\t\t}\r\n\t\t}\r\n\t});\r\n\t\r\n\n\r\n\t/*--- TAG ANALYTICS UNIVERSAL ---*/\r\n\t\r\n\t(function(i,s,o,g,r,a,m){i[\'GoogleAnalyticsObject\']=r;i[r]=i[r]||function(){\r\n\t(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),\r\n\tm=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)\r\n\t})(window,document,\'script\',\'//www.google-analytics.com/analytics.js\',\'ga\');\r\n\r\n\tga(\'create\', \'UA-5650410-1\', \'auto\');\r\n\tvar url_tracking \t= window.location.href;\r\n\tvar title_tracking \t= window.document.title;\r\n\tif(url_tracking && title_tracking){\r\n\t\turl_tracking \t= (url_tracking).replace(/http:\\/\\/(www|m)\\.sbt\\.com\\.br/gi,\'\');\r\n\t\tga(\'set\', \'page\', url_tracking);\r\n\t\tga(\'set\', \'title\', title_tracking);\t\t\r\n\t}\r\n\r\n\t\r\n\t\tga(\'set\', \'domain_name\', \'www.sbt.com.br\');\r\n\t\t\r\n\r\n\tga(\'send\', \'pageview\', {\r\n\t\t\'dimension1\': \t\'www.sbt.com.br\'\t\t\r\n\t});\r\n\t/*-------------------------------*/\r\n\n\n\r\n  var _comscore = _comscore || [];\r\n  _comscore.push({ c1: "2", c2: "17692091" });\r\n  (function() {\r\n    var s = document.createElement("script"), el = document.getElementsByTagName("script")[0]; s.async = true;\r\n    s.src = (document.location.protocol == "https:" ? "https://sb" : "http://b") + ".scorecardresearch.com/beacon.js";\r\n    el.parentNode.insertBefore(s, el);\r\n  })();\r\n\n\n\n\n\n\n\r\n\t(function(t,c,k) {\r\n\t\tvar s \t= document.createElement("script");\r\n\t\tvar el \t= document.getElementsByTagName("script")[0];\r\n\t\ts.async = true;\r\n\t\ts.src \t= (("https:" == document.location.protocol) ? "https://" : "http://") + \'www.dataunion.com.br/\' + t + \'/\' + (c || \'\') + (k?(\'/\'+k):\'\');\r\n\t\tel.parentNode.insertBefore(s, el);\r\n\t})(\'2b3ed8c1-8661-491c-9543-869d56dd5f05\');\r\n\n\n\n' 
