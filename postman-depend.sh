#!/bin/sh

brew install node
echo 'Node Installed Successfully'

# npm install -g jaiman

npm install -g newman
echo 'Newman Installed Successfully'

npm install -g newman-reporter-htmlextra
echo 'htmlextra installed successfully'

npm install -g @apideck/postman-to-k6
echo 'k6 installed successfully'

echo 'list of npm packages installed'
npm list -g