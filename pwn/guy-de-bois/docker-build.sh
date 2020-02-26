docker build ./setup -t ccsc2020/guy-de-bois
CID=$(docker create ccsc2020/guy-de-bois)
docker cp ${CID}:/home/ctf/chall ./public/chall
docker rm ${CID}