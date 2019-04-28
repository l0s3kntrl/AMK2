# -*- coding: utf-8 -*-


import urlparse,sys,urllib,xbmc,os,xbmcaddon,xbmcgui
from resources.lib.modules import log_utils,control,trakt

dialog = xbmcgui.Dialog()

params = dict(urlparse.parse_qsl(sys.argv[2].replace('?','')))

action = params.get('action')

subid = params.get('subid')

docu_category = params.get('docuCat')

docu_watch = params.get('docuPlay')

podcast_show = params.get('podcastshow')

podcast_cat = params.get('podcastlist')

podcast_cats = params.get('podcastcategories')

podcast_episode = params.get('podcastepisode')

name = params.get('name')

title = params.get('title')

year = params.get('year')

imdb = params.get('imdb')

tvdb = params.get('tvdb')

tmdb = params.get('tmdb')

season = params.get('season')

episode = params.get('episode')

tvshowtitle = params.get('tvshowtitle')

premiered = params.get('premiered')

url = params.get('url')

image = params.get('image')

meta = params.get('meta')

select = params.get('select')

query = params.get('query')

source = params.get('source')

content = params.get('content')

windowedtrailer = params.get('windowedtrailer')
windowedtrailer = int(windowedtrailer) if windowedtrailer in ("0","1") else 0


if action == None:
    from resources.lib.indexers import navigator
    from resources.lib.modules import cache
    cache.cache_version_check()
    navigator.navigator().root()

elif action == 'movieNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().movies()

elif action == 'movieliteNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().movies(lite=True)

elif action == 'mymovieNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().mymovies()

elif action == 'mymovieliteNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().mymovies(lite=True)

elif action == 'tvNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().tvshows()

elif action == 'tvliteNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().tvshows(lite=True)

elif action == 'mytvNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().mytvshows()

elif action == 'mytvliteNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().mytvshows(lite=True)

elif action == 'wtfNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().wtf()

elif action == 'wtfliteNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().wtf(lite=True)	

elif action == 'moreplugs':
    from resources.lib.indexers import navigator
    navigator.navigator().moreplugs()

elif action == 'wtfMovies':
    from resources.lib.indexers import navigator
    navigator.navigator().wtfMovies()
	
elif action == 'wtfShows':
    from resources.lib.indexers import navigator
    navigator.navigator().wtfShows()

elif action == 'movieMosts':
    from resources.lib.indexers import navigator
    navigator.navigator().movieMosts()

elif action == 'showMosts':
    from resources.lib.indexers import navigator
    navigator.navigator().showMosts()
	
elif action == 'playlistNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().playlist()

elif action == 'playlistliteNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().playlist(lite=True)

elif action == 'spikeNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().spike()
	
elif action == 'spikeliteNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().spike(lite=True)

elif action == 'customNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().custom()
	
elif action == 'customliteNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().custom(lite=True)

elif action == 'imdbLists':
    from resources.lib.indexers import navigator
    navigator.navigator().imdbLists()	

elif action == 'critterLists':
    from resources.lib.indexers import navigator
    navigator.navigator().critterLists()

elif action == 'JewNavigator':
    from resources.lib.indexers import navigator2
    navigator2.navigator().root()

elif action == 'myuranmvNavigator':
    from resources.lib.indexers import navigator2
    navigator2.navigator().myuranmv()

elif action == 'myholidmvNavigator':
    from resources.lib.indexers import navigator2
    navigator2.navigator().myholidmv()

elif action == 'mysupermvNavigator':
    from resources.lib.indexers import navigator2
    navigator2.navigator().mysupermv()

elif action == 'myurantvNavigator':
    from resources.lib.indexers import navigator2
    navigator2.navigator().myurantv()

elif action == 'boxesNavigator':
    from resources.lib.indexers import navigator2
    navigator2.navigator().boxes()

elif action == 'myclassicsNavigator':
    from resources.lib.indexers import navigator2
    navigator2.navigator().myclassics()

elif action == 'mymoreNavigator':
    from resources.lib.indexers import navigator2
    navigator2.navigator().mymore()

elif action == 'movies2':
    from resources.lib.indexers import movies2
    movies2.movies().get(url)

elif action == 'tvshows2':
    from resources.lib.indexers import tvshows2
    tvshows2.tvshows().get(url)

elif action == 'downloadNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().downloads()

elif action == 'libraryNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().library()

elif action == 'toolNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().tools()

elif action == 'searchNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().search()

elif action == 'viewsNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().views()

elif action == 'clearCache':
    from resources.lib.indexers import navigator
    navigator.navigator().clearCache()

elif action == 'clearAllCache':
    from resources.lib.indexers import navigator
    navigator.navigator().clearCacheAll()

elif action == 'clearMetaCache':
    from resources.lib.indexers import navigator
    navigator.navigator().clearCacheMeta()
	
elif action == 'clearCacheSearch':
    from resources.lib.indexers import navigator
    navigator.navigator().clearCacheSearch()

elif action == 'infoCheck':
    from resources.lib.indexers import navigator
    navigator.navigator().infoCheck('')

elif action == 'movies':
    from resources.lib.indexers import movies
    movies.movies().get(url)

elif action == 'moviePage':
    from resources.lib.indexers import movies
    movies.movies().get(url)

elif action == 'movieWidget':
    from resources.lib.indexers import movies
    movies.movies().widget()

elif action == 'movieSearch':
    from resources.lib.indexers import movies
    movies.movies().search()

elif action == 'movieSearchnew':
    from resources.lib.indexers import movies
    movies.movies().search_new()

elif action == 'movieSearchterm':
    from resources.lib.indexers import movies
    movies.movies().search_term(name)

elif action == 'moviePerson':
    from resources.lib.indexers import movies
    movies.movies().person()

elif action == 'movieGenres':
    from resources.lib.indexers import movies
    movies.movies().genres()

elif action == 'movieLanguages':
    from resources.lib.indexers import movies
    movies.movies().languages()

elif action == 'movieCertificates':
    from resources.lib.indexers import movies
    movies.movies().certifications()

elif action == 'movieYears':
    from resources.lib.indexers import movies
    movies.movies().years()

elif action == 'moviePersons':
    from resources.lib.indexers import movies
    movies.movies().persons(url)

elif action == 'movieUserlists':
    from resources.lib.indexers import movies
    movies.movies().userlists()

elif action == 'tvshows':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().get(url)

elif action == 'tvshowPage':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().get(url)

elif action == 'tvSearch':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().search()

elif action == 'tvSearchnew':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().search_new()

elif action == 'tvSearchterm':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().search_term(name)

elif action == 'tvPerson':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().person()

elif action == 'tvGenres':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().genres()

elif action == 'tvNetworks':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().networks()

elif action == 'tvLanguages':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().languages()

elif action == 'tvCertificates':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().certifications()

elif action == 'tvPersons':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().persons(url)

elif action == 'tvUserlists':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().userlists()

elif action == 'seasons':
    from resources.lib.indexers import episodes
    episodes.seasons().get(tvshowtitle, year, imdb, tvdb)

elif action == 'episodes':
    from resources.lib.indexers import episodes
    episodes.episodes().get(tvshowtitle, year, imdb, tvdb, season, episode)

elif action == 'calendar':
    from resources.lib.indexers import episodes
    episodes.episodes().calendar(url)

elif action == 'tvWidget':
    from resources.lib.indexers import episodes
    episodes.episodes().widget()

elif action == 'calendars':
    from resources.lib.indexers import episodes
    episodes.episodes().calendars()

elif action == 'episodeUserlists':
    from resources.lib.indexers import episodes
    episodes.episodes().userlists()

elif action == 'tvReviews':
    from resources.lib.indexers import youtube
    if subid == None:
        youtube.yt_index().root(action)
    else:
        youtube.yt_index().get(action, subid)

elif action == 'movieReviews':
    from resources.lib.indexers import youtube
    if subid == None:
        youtube.yt_index().root(action)
    else:
        youtube.yt_index().get(action, subid)

elif action == 'refresh':
    from resources.lib.modules import control
    control.refresh()

elif action == 'queueItem':
    from resources.lib.modules import control
    control.queueItem()

elif action == 'openSettings':
    from resources.lib.modules import control
    control.openSettings(query)

elif action == 'artwork':
    from resources.lib.modules import control
    control.artwork()

elif action == 'addView':
    from resources.lib.modules import views
    views.addView(content)

elif action == 'moviePlaycount':
    from resources.lib.modules import playcount
    playcount.movies(imdb, query)

elif action == 'episodePlaycount':
    from resources.lib.modules import playcount
    playcount.episodes(imdb, tvdb, season, episode, query)

elif action == 'tvPlaycount':
    from resources.lib.modules import playcount
    playcount.tvshows(name, imdb, tvdb, season, query)

elif action == 'trailer':
    from resources.lib.modules import trailer
    trailer.trailer().play(name, url, windowedtrailer)

elif action == 'traktManager':
    from resources.lib.modules import trakt
    trakt.manager(name, imdb, tvdb, content)

elif action == 'authTrakt':
    from resources.lib.modules import trakt
    trakt.authTrakt()

elif action == 'smuSettings':
    try: import resolveurl
    except: pass
    resolveurl.display_settings()

elif action == 'urlResolver':
    try: import resolveurl
    except: pass
    resolveurl.display_settings()

elif action == 'download':
    import json
    from resources.lib.modules import sources
    from resources.lib.modules import downloader
    try: downloader.download(name, image, sources.sources().sourcesResolve(json.loads(source)[0], True))
    except: pass
	
elif action == 'docuHeaven':
    from resources.lib.indexers import docu
    if not docu_category == None:
        docu.documentary().docu_list(docu_category)
    elif not docu_watch == None:
        docu.documentary().docu_play(docu_watch)
    else:
        docu.documentary().root()

elif action == 'kidscorner':
    from resources.lib.indexers import youtube
    if subid == None:
        youtube.yt_index().root(action)
    else:
        youtube.yt_index().get(action, subid)

elif action == 'fitness':
    from resources.lib.indexers import youtube
    if subid == None:
        youtube.yt_index().root(action)
    else:
        youtube.yt_index().get(action, subid)

elif action == 'legends':
    from resources.lib.indexers import youtube
    if subid == None:
        youtube.yt_index().root(action)
    else:
        youtube.yt_index().get(action, subid)

elif action == 'podcastNavigator':
    from resources.lib.indexers import podcast
    podcast.podcast().root()

elif action == 'podbay':
    from resources.lib.indexers import podcast
    if not podcast_show == None:
        podcast.podcast().pb_show(podcast_show)
    elif not podcast_cat == None:
        podcast.podcast().pb_cat(podcast_cat)
    elif not podcast_cats == None:
        podcast.podcast().pb_root()
    elif not podcast_episode == None:
        podcast.podcast().podcast_play(action, podcast_episode)
    else:
        podcast.podcast().pb_root()

elif action == 'podcastOne':
    from resources.lib.indexers import podcast
    if not podcast_show == None:
        podcast.podcast().pco_show(podcast_show)
    elif not podcast_cat == None:
        podcast.podcast().pco_cat(podcast_cat)
    elif not podcast_cats == None:
        podcast.podcast().pcocats_list()
    elif not podcast_episode == None:
        podcast.podcast().podcast_play(action, podcast_episode)
    else:
        podcast.podcast().pco_root()

elif action == 'radios':
    from resources.lib.indexers import tunes
    tunes.radios()
 
elif action == 'radioResolve':
    from resources.lib.indexers import tunes
    tunes.radioResolve(url)
 
elif action == 'radio1fm':
    from resources.lib.indexers import tunes
    tunes.radio1fm()
 
elif action == 'radio181fm':
    from resources.lib.indexers import tunes
    tunes.radio181fm()

if action == 'jewMC':
    from resources.lib.indexers import lists
    lists.indexer().rootMC()

if action == 'iptvChannels':
    from resources.lib.indexers import lists
    lists.indexer().root()

if action == 'navXXX':
    from resources.lib.indexers import lists
    lists.indexer().rootXXX()

elif action == 'directory':
    from resources.lib.indexers import lists
    lists.indexer().get(url)

elif action == 'qdirectory':
    from resources.lib.indexers import lists
    lists.indexer().getq(url)

elif action == 'xdirectory':
    from resources.lib.indexers import lists
    lists.indexer().getx(url)

elif action == 'developer':
    from resources.lib.indexers import lists
    lists.indexer().developer()

elif action == 'tvtuner':
    from resources.lib.indexers import lists
    lists.indexer().tvtuner(url)

elif 'youtube' in str(action):
    from resources.lib.indexers import lists
    lists.indexer().youtube(url, action)

elif action == 'browser':
    from resources.lib.indexers import lists
    lists.resolver().browser(url)

elif action == 'play':
    from resources.lib.modules import sources
    from resources.lib.indexers import lists
    if not content == None:
        lists.player().play(url, content)
    else:
        sources.sources().play(title, year, imdb, tvdb, season, episode, tvshowtitle, premiered, meta, select)

elif action == 'addItem':
    from resources.lib.modules import sources
    sources.sources().addItem(title)

elif action == 'playItem':
    from resources.lib.modules import sources
    sources.sources().playItem(title, source)

elif action == 'alterSources':
    from resources.lib.modules import sources
    sources.sources().alterSources(url, meta)

elif action == 'clearSources':
    from resources.lib.modules import sources
    sources.sources().clearSources()

elif action == 'disableAll':
    from resources.lib.modules import sources
    sources.sources().disableAll()

elif action == 'enableAll':
    from resources.lib.modules import sources
    sources.sources().enableAll()

elif action == 'random':
    rtype = params.get('rtype')
    if rtype == 'movie':
        from resources.lib.indexers import movies
        rlist = movies.movies().get(url, create_directory=False)
        r = sys.argv[0]+"?action=play"
    elif rtype == 'episode':
        from resources.lib.indexers import episodes
        rlist = episodes.episodes().get(tvshowtitle, year, imdb, tvdb, season, create_directory=False)
        r = sys.argv[0]+"?action=play"
    elif rtype == 'season':
        from resources.lib.indexers import episodes
        rlist = episodes.seasons().get(tvshowtitle, year, imdb, tvdb, create_directory=False)
        r = sys.argv[0]+"?action=random&rtype=episode"
    elif rtype == 'show':
        from resources.lib.indexers import tvshows
        rlist = tvshows.tvshows().get(url, create_directory=False)
        r = sys.argv[0]+"?action=random&rtype=season"
    from resources.lib.modules import control
    from random import randint
    import json
    try:
        rand = randint(1,len(rlist))-1
        for p in ['title','year','imdb','tvdb','season','episode','tvshowtitle','premiered','select']:
            if rtype == "show" and p == "tvshowtitle":
                try: r += '&'+p+'='+urllib.quote_plus(rlist[rand]['title'])
                except: pass
            else:
                try: r += '&'+p+'='+urllib.quote_plus(rlist[rand][p])
                except: pass
        try: r += '&meta='+urllib.quote_plus(json.dumps(rlist[rand]))
        except: r += '&meta='+urllib.quote_plus("{}")
        if rtype == "movie":
            try: control.infoDialog(rlist[rand]['title'], control.lang(32536).encode('utf-8'), time=30000)
            except: pass
        elif rtype == "episode":
            try: control.infoDialog(rlist[rand]['tvshowtitle']+" - Season "+rlist[rand]['season']+" - "+rlist[rand]['title'], control.lang(32536).encode('utf-8'), time=30000)
            except: pass
        control.execute('RunPlugin(%s)' % r)
    except:
        control.infoDialog(control.lang(32537).encode('utf-8'), time=8000)

elif action == 'movieToLibrary':
    from resources.lib.modules import libtools
    libtools.libmovies().add(name, title, year, imdb, tmdb)

elif action == 'moviesToLibrary':
    from resources.lib.modules import libtools
    libtools.libmovies().range(url)

elif action == 'moviesToLibrarySilent':
    from resources.lib.modules import libtools
    libtools.libmovies().silent(url)

elif action == 'tvshowToLibrary':
    from resources.lib.modules import libtools
    libtools.libtvshows().add(tvshowtitle, year, imdb, tvdb)

elif action == 'tvshowsToLibrary':
    from resources.lib.modules import libtools
    libtools.libtvshows().range(url)

elif action == 'tvshowsToLibrarySilent':
    from resources.lib.modules import libtools
    libtools.libtvshows().silent(url)

elif action == 'updateLibrary':
    from resources.lib.modules import libtools
    libtools.libepisodes().update(query)

elif action == 'service':
    from resources.lib.modules import libtools
    libtools.libepisodes().service()

elif action == 'ShowChangelog':
    from resources.lib.modules import changelog
    changelog.get()	

###Dev Lazy Tools###
elif action == 'TurnOnDbird':
    if xbmcaddon.Addon('script.module.resolveurl').getSetting('RealDebridResolver_enabled') != 'true':
        try:
            xbmcaddon.Addon('script.module.resolveurl') .setSetting(id='RealDebridResolver_enabled', value='true')
        except: pass
        dialog.notification('Turn On RealDebridResolver', 'Done, Setting Enabled.', xbmcgui.NOTIFICATION_INFO, 5000)
        
elif action == 'TurnOffDbird':
    if xbmcaddon.Addon('script.module.resolveurl').getSetting('RealDebridResolver_enabled') != 'false':
        try:
            xbmcaddon.Addon('script.module.resolveurl') .setSetting(id='RealDebridResolver_enabled', value='false')
        except: pass
        dialog.notification('Turn Off RealDebridResolver', 'Done, Setting Disabled.', xbmcgui.NOTIFICATION_INFO, 5000)

elif action == 'TurnOnPreMe':
    if xbmcaddon.Addon('script.module.resolveurl').getSetting('PremiumizeMeResolver_enabled') != 'true':
        try:
            xbmcaddon.Addon('script.module.resolveurl') .setSetting(id='PremiumizeMeResolver_enabled', value='true')
        except: pass
        dialog.notification('Turn On PremiumizeMeResolver', 'Done, Setting Enabled.', xbmcgui.NOTIFICATION_INFO, 5000)
        
elif action == 'TurnOffPreMe':
    if xbmcaddon.Addon('script.module.resolveurl').getSetting('PremiumizeMeResolver_enabled') != 'false':
        try:
            xbmcaddon.Addon('script.module.resolveurl') .setSetting(id='PremiumizeMeResolver_enabled', value='false')
        except: pass
        dialog.notification('Turn Off PremiumizeMeResolver', 'Done, Setting Disabled.', xbmcgui.NOTIFICATION_INFO, 5000)

elif action == 'TipsPlaceHolder':
	control.infoDialog(control.lang(101011).encode('utf-8'), sound=True, icon='INFO')

elif action == 'PairEm':
    from resources.lib.indexers import pairem
    pairem.pairmenuoptions()

elif action == 'devtoolNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().devtools()

