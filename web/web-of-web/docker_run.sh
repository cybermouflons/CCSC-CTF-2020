if [[ -z "$1" ]]; then
    echo "I need the external IP of the container"
    echo "Run again with: ./docker_run.sh X.X.X.X"
    exit
fi

docker run -e "EXTERNAL_IP=$1" -p 5001:5001 -p 9999:9999 -d ccsc2020/webofweb

