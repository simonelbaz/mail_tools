while read uid
do
	dnvar=$(ldapsearch -x -H 'ldaps://172.17.2.8' -D 'xxxx' -w 'xxx' -b 'xxxx' "(uid=$uid)" dn | sed -n -e '/^dn/ { N;}' -e 's/\n //gp' )
	if [ "$dnvar" != "" ];
	then
		echo $dnvar
		echo "changetype: modify"
		echo "add: thumbnailPhoto"
		echo "thumbnailPhoto:< file:///var/lib/photos/$uid.jpg"
		#echo "--"
	fi
done < liste_people.txt
