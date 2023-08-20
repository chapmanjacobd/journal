#!/bin/bash
tmux new -s work -d
tmux rename-window -t work logs
tmux send-keys -t work 'cd $BASE_DIR && vagrant up && tmux send-keys -t work:vm "cd $BASE_DIR && vagrant ssh" C-m && vagrant ssh' C-m 'pm2 log' C-m
tmux new-window -t work
tmux rename-window -t work vm
tmux new-window -t work
tmux rename-window -t work term
tmux send-keys -t work 'cd $BASE_DIR && git pull' C-m
tmux attach -t work
