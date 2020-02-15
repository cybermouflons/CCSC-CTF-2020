docker build ./setup -t ccsc2020/spell-caster
CID=$(docker create ccsc2020/spell-caster)
docker cp ${CID}:/home/ctf/chall ./public/chall
docker rm ${CID}