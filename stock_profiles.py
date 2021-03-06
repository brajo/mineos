"""A python script to manage minecraft servers
   Designed for use with MineOS: http://minecraft.codeemo.com
"""

__author__ = "William Dizon"
__license__ = "GNU GPL v3.0"
__version__ = "0.6.0"
__email__ = "wdchromium@gmail.com"
 
STOCK_PROFILES = {
    'vanilla174': {
        'name': 'vanilla174',
        'type': 'standard_jar',
        'url': 'https://s3.amazonaws.com/Minecraft.Download/versions/1.7.4/minecraft_server.1.7.4.jar',
        'save_as': 'minecraft_server.1.7.4.jar',
        'run_as': 'minecraft_server.1.7.4.jar',
        'ignore': '',
        'desc': 'official minecraft_server.jar'
        },
    'vanilla164': {
        'name': 'vanilla164',
        'type': 'standard_jar',
        'url': 'https://s3.amazonaws.com/Minecraft.Download/versions/1.6.4/minecraft_server.1.6.4.jar',
        'save_as': 'minecraft_server.jar',
        'run_as': 'minecraft_server.jar',
        'ignore': '',
        'desc': 'official minecraft_server.jar'
        }, 
    'bukkit-recommended': {
        'name': 'bukkit-recommended',
        'type': 'standard_jar',
        'url': 'http://dl.bukkit.org/latest-rb/craftbukkit.jar',
        'save_as': 'craftbukkit.jar',
        'run_as': 'craftbukkit.jar',
        'ignore': '',
        }, 
    'bukkit-beta': {
        'name': 'bukkit-beta',
        'type': 'standard_jar',
        'url': 'http://dl.bukkit.org/latest-beta/craftbukkit.jar',
        'save_as': 'craftbukkit.jar',
        'run_as': 'craftbukkit.jar',
        'ignore': '',
        }, 
    'bukkit-dev': {
        'name': 'bukkit-dev',
        'type': 'standard_jar',
        'url': 'http://dl.bukkit.org/latest-dev/craftbukkit.jar',
        'save_as': 'craftbukkit.jar',
        'run_as': 'craftbukkit.jar',
        'ignore': '',
        }
    'spigot': {
        'name': 'spigot',
        'type': 'standard_jar',
        'url': 'http://ci.md-5.net/job/Spigot/lastSuccessfulBuild/artifact/Spigot-Server/target/spigot.jar',
        'save_as': 'spigot.jar',
        'run_as': 'spigot.jar',
        'ignore': '',
        }
    }
