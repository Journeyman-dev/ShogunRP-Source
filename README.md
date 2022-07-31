# ShogunRP Source

This is the source code of ShogunRP module for Mount and Blade: Warband. It was used for Felix's LegionRP server in the summer of 2017. The code is built upon the persistent world module by Steven Schwartfeger (Vornne) which can be found [https://github.com/vornne/pw_module_system](https://github.com/vornne/pw_module_system). The mod itself, along with all asset files, can be downloaded from Nexus Mods: [https://www.nexusmods.com/mbwarband/mods/6162](https://www.nexusmods.com/mbwarband/mods/6162). All coding was done by Daniel Valcour (Journeyman, known as Ramaraunt back when this was made). The map was designed by Jhorj, and the menu artwork was designed by SHURIKIN. Most of the japanese props and items were taken from the Gokokujo mod with permission from phlpp, the author of that mod.

There are also over 100 different open source packages, commonly refeered to by the community as OSPs, which are as follows:

- Vornne and others - Credit goes to the creators of PW mod. View all of them here:
  - Laszlo: inspiration from the early versions of PW, discussion of ideas, and testing.
  - Vornne: main developer for the version of Persistent World used to make ShogunRP.
  - Joss: converting native armour textures to heraldic format, some new meshes, and testing.
  - Blobmania: new meshes for sign posts, construction boxes, and some food resources.
  - Austro: new meshes for iron mines and ores, silver and gold mines, and various rocks.
  - The Bowman: enterable houses adapted from native meshes, a ferry boat.
  - Mandible: meshes for constructing tunnels.
  - Yamabusi: new priest, bishop, and surgeon clothing meshes.
  - Highlander: boar and deer meshes from Age of Machinery (an old M&B mod).
  - thortheviking: loading and menu background images.
  - PapaLazarou: frames from his crouching animation that were adapted to suit PW.
  - Lyndon Daniels: static cow mesh, rigged by Vornne.
  - The Taleworlds developers: for helpfulness with feature requests, particularly versions 1.134 and 1.142, and for inspiration from the native module system.
  - Vincenzo: for helping drive many new warband releases - without which a lot of the scripting would be much harder or impossible; also help with testing and bug reporting.
- SacredStoneHead: for the "SSH Samurai Armour Set OSP", which is used in
this mod. Link: http://www.nexusmods.com/mbwarband/mods/3666/?
- bogmir: for the "Samurai weapons OSP", which can be found here:
https://forums.taleworlds.com/index.php/topic,210160.0.html
- xenoargh: for the for the "Camel OSP". It can be found here:
https://forums.taleworlds.com/index.php/topic,114455.0.html
- as0017: for the "Some Vietnamese Items OSP". It can be found here:
https://forums.taleworlds.com/index.php/topic,198052.0.html
- Llew: for the "Flintlock Firearms OSP". It can be found here:
https://www.mbrepository.com/file.php?id=2699
- Shcherbyna: for the "Nobori (vertical) banners pack" found here:
https://www.mbrepository.com/file.php?id=2674
- Alex Dragon 's ROTK Team, 猫大, & William Berne: Creators of the "Elephant OSP". Link:
http://www.nexusmods.com/mountandblade/mods/3449/?
- cmpxchg8b: for help with understanding how the game engine works underneath the module system, and for the WSE profiling tool.
- mtarini: for creating OpenBRF and fixing reported bugs very quickly.
- Clint Bellanger - for the onion model and texture.
- TrekkieGrrrl - for sushi model. Cannot be used for commercial projects. See attached readme for details "sushi_readme".
- dogbrand - for doctor mask. http://www.thingiverse.com/thing:1278435/#comments
- Keedo and theAthenian - Zombie model a nd textures. Taken from native overhaul mod.
- SPAK - spak items OSP
- Barf - SKELETON ARMY OSP
- Llew and Dain - LOTR Weapons OSP https://forums.taleworlds.com/index.php/topic,68456.msg1771058.html
- suicidecrew - Fire texture (from deviantart)
- Berengar - Berengar's gothic armors OSP
- IYIORT - IYIORT's Desert Island OSP
- rodoedan and cwr - White walker OSP

# Features

On top of the original features built into Persistent World, ShogunRP module adds the following:

* New props and equipment, with meshes taken from various mod creators (with their permission). The new weapons and armor were balanced with the help of community testers.
* Over 10 new kinds of food, with methods of production. This includes rice, sake, cabbages, carrots, potatos, mushrooms (with poisinous and rare truffle variants), soy beans (and sauce), and sushi. These foods have different stations placed around the default map where they can be gathered, grown, cooked, and crafted.
* A hunger system, requiring players to occasionally eat food to not starve to death. This can be disabled in the module configuration file.
* A disease system, where players can gain various aliments and conditions such as drunkeness, the common cold, the flu, and the plague.
* A necromancy system, which admins can use to raise players as undead NPCs and then command them.
* Balance changes to the existing PW money chest thievery system to enourage more players to utilize it and incentivize player factions to leave money in the chests to defend, while also providing factions with passive income.
* Costumes which admins can spawn for roleplaying as various mythical creatures.
