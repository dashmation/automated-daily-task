#!/bin/bash

onboarding=$(grep -i 'Vold 3.0 (the awakening) firing up' attempt6.txt)
home=$(grep -i 'MainActivity: createLauncherMenuFragment: is forked ?  : false' attempt6.txt)

onboaring_time=${onboarding:5:14}
home_time=${home:5:14}

final='expr $home_time - $onboaring_time'
echo $final