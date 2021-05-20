spoof:
	node data_spoof/send_data.js

heartbleed:
	python heartbleed.py localhost -p 8443 | less

bcopy:
	docker cp ./server/www 6cd958064724:/var/

mcopy:
	docker cp ./server/www 0be0960f6137:/var/
