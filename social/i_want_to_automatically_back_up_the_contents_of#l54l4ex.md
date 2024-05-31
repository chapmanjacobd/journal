Sorry, you're right. You also need to enable ignoreDelete on the backup computer in advance settings: https://docs.syncthing.net/advanced/folder-ignoredelete.html

If you ever wanted to sync deletes _after_ enabling that you would need to re-setup the sync folder because the option messes up the sync index but given that you would be using Send Only and Receive Only on the backup computer this shouldn't be an issue
