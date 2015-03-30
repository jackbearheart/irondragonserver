#!/bin/sh

curl -XPOST http://localhost:8000/api -d '{"cmd":"create-game","game_id":1}'
