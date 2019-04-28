# -*- coding: utf-8 -*-

import threading
from resources.lib.modules import control,log_utils,trakt

control.execute('RunPlugin(plugin://%s)' % control.get_plugin_url({'action': 'service'}))

def syncTraktLibrary():
    control.execute('RunPlugin(plugin://%s)' % 'plugin.video.kongtv/?action=tvshowsToLibrarySilent&url=traktcollection')
    control.execute('RunPlugin(plugin://%s)' % 'plugin.video.kongtv/?action=moviesToLibrarySilent&url=traktcollection')
try:
    AddonVersion = control.addon('plugin.video.kongtv').getAddonInfo('version')
    ModuleVersion = control.addon('script.module.kongtv').getAddonInfo('version')
    RepoVersion = control.addon('repository.StarTec').getAddonInfo('version')
    log_utils.log('===-[AddonVersion: %s]-' % str(AddonVersion) + '-[ModuleVersion: %s]-' % str(ModuleVersion) + '-[RepoVersion: %s]-' % str(RepoVersion), log_utils.LOGNOTICE)
except:
    log_utils.log('===-[Error Oppps...', log_utils.LOGNOTICE)
    log_utils.log('===-[Had Trouble Getting Version Info. Make Sure You Have the StarTec.', log_utils.LOGNOTICE)
if control.setting('autoTraktOnStart') == 'true':
    syncTraktLibrary()
if int(control.setting('schedTraktTime')) > 0:
    log_utils.log('===-[Kong Tv - Starting Trakt Scheduling.', log_utils.LOGNOTICE)
    log_utils.log('===-[Kong Tv - Scheduled Time Frame '+ control.setting('schedTraktTime')  + ' Hours.', log_utils.LOGNOTICE)
    timeout = 3600 * int(control.setting('schedTraktTime'))
    schedTrakt = threading.Timer(timeout, syncTraktLibrary)
    schedTrakt.start()


