# coding=utf-8
"""
Script Name: defaultVariable.py
Author: Do Trinh/Jimmy - 3D artist, leader DAMG team.

Description:
    This script is the place that all the variables will be referenced from here
"""
# -------------------------------------------------------------------------------------------------------------
# IMPORT PYTHON MODULES
# -------------------------------------------------------------------------------------------------------------
import os, sys, winshell, platform
from tk import message

# ------------------------------------------------------
# DEFAULT VARIABLES
# ------------------------------------------------------
# encode.py
STRINPUT = 'password'
HEXINPUT = '70617373776F7264'
ENCODE = ['hexadecimal', 'ascii', 'unicode']
OPERATION = dict( encode=[ 'hex', 'string' ], pathInfo=[ 'create', 'read', 'modify' ] )

# getData.py
MAIN_NAMES = dict( info='apps.pipeline',
                   log='log.pipeline',
                   web='webs.pipeline',
                   maya='maya.pipeline',
                   mayaEnv = 'env.maya',
                   appdata=['appData', 'PipelineInfo'],
                   sysEnv = 'env.os',
                   )

def createInfo():
    appDir = os.getenv('LOCALAPPDATA' ).split( 'Local' )[0]
    infoDir = os.path.join( appDir, MAIN_NAMES['appdata'][1])
    if not os.path.exists( infoDir ):
        os.makedirs( infoDir )
    return infoDir

inforDir = createInfo()

USERNAME = platform.node()

MAIN_ID = dict( Main='Pipeline Manager',
                About='About pipeline application',
                Credit='Credit')

APPDATA = [inforDir, os.path.join(os.getcwd().split('ui')[0], MAIN_NAMES['appdata'][0]),]

MAIN_MESSAGE = dict( About=message.MAIN_ABOUT,
                     Credit=message.MAIN_CREDIT,
                     status='Pipeline Application', )

MAIN_TABID = ['', 'Production Info', 'Sub Tools', 'Tool Box']

MAIN_PLUGIN = dict( winshell='winshell' )

MAIN_URL = dict( Help='https://github.com/vtta2008/DAMGpipeline', )

MAIN_PACKPAGE = dict( job=[ 'TD', 'Comp', 'Design', 'Office', 'UV', 'Sound' ],
                      TD=[ 'Maya', '3Ds max', 'Mudbox', 'Houdini FX', 'ZBrush', 'Mari' ],
                      Comp=[ 'NukeX', 'Hiero', 'After Effects', 'Premiere Pro' ],
                      Design=[ 'Photoshop', 'Illustrator', 'InDesign' ],
                      Office=[ 'Word', 'Excel', 'PowerPoint' ],
                      UV=[ 'UVLayout' ],
                      Sound=[ 'Audition' ],
                      instruction=[ 'documentation' ],
                      website=[ 'doc' ],
                      image=[ 'icons', 'imgs' ],
                      py=[ 'tk', 'ui', 'plugins', '' ],
                      ext=[ '.exe', 'InitTool.py', '.lnk' ],
                      sysOpts=[ "Host Name", "OS Name", "OS Version", "Product ID", "System Manufacturer",
                                "System Model",
                                "System type", "BIOS Version", "Domain", "Windows Directory", "Total Physical Memory",
                                "Available Physical Memory", "Logon Server" ],
                      temp=os.path.join(os.getcwd(), 'temp'),
                      info=os.path.join(os.getcwd().split( 'ui' )[ 0 ], 'appData'),
                      desktop=winshell.desktop(),
                      current=os.getcwd(),
                      root=os.getcwd().split( 'ui' )[ 0 ],
                      appData=APPDATA[ 0 ],
                      filter=[ 'Non-commercial', 'Uninstall', 'Verbose', 'License', 'Skype' ],
                      adobe=[ 'CS5', 'CS6', 'CC' ],
                      geo=[ 300, 300, 300, 400, 350], )

MAIN_ROOT = dict(main=MAIN_PACKPAGE['root'])