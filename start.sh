curlftpfs $SERVER_ADDRESS /mnt -o user=$FTP_USER:$FTP_PASS,allow_other &
python3 app.py