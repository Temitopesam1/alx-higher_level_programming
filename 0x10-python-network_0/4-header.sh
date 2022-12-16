#!/bin/bash
# Script that takes an URL and displays the body of the response
#curl -s "$1" -H "X-HolbertonSchool-User-Id: 98"
curl -s -H "X-School-User-Id: 98" $1
