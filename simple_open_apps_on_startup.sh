#!/bin/zsh

echo "\nOpening OneDrive."

cd /Applications && open OneDrive.app && sleep 1

one_d_ecode=$?

pids=($(pgrep OneDrive))

echo $pids

max=$pids[1]

for i in $pids; do
	if [ $i -ge $max ]; then
	max=$i
	fi
done

echo "Killing: $max."
kill $max

if [ $one_d_ecode -eq '0' ]; then
	echo "OneDrive opened successfully.\n"
fi

echo "Opening Teams."

open Microsoft\ Teams.app

teams_ecode=$?

if [ $teams_ecode -eq '0' ]; then
	echo "Teams opened successfully.\n"
fi

open Microsoft\ Outlook.app

outlook_ecode=$?

echo "Opening Outlook."

if [ $outlook_ecode -eq '0' ]; then
	echo "Outlook opened successfully.\n"
fi




