#!/bin/bash
# GMSeal up

cd /root
GMSealName=GMSeal
NewGMSeal="publish*.zip"
GMSealNum=`ls -l | grep "GMSeal*" | grep "^d" | wc -l`
OldGMSeal=GMSeal-${GMSealNum}
unzip $NewGMSeal
NewGMSeal=publish

mv $GMSealName $OldGMSeal
mv $NewGMSeal $GMSealName
echo "Folder modification completed"
cd /root/${OldGMSeal}
ConfigFile=appsettings.json
SoFileX86=libloadswsds-x86.so
SoFileX64=libloadswsds-x64.so
GMSealDatabase=testnetcore.db
LicFile=Lic
cp -r ${ConfigFile} ${SoFileX86} ${SoFileX64} ${GMSealDatabase} ${LicFile} /root/GMSeal/
echo "Database configuration completed"
systemctl restart supervisord
echo "Please enter "http://ipserver" to visit the webpage"
