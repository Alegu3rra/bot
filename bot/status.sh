#!/bin/bash
status=$(service mysql status | grep "active" | awk '{print $2}')
echo $status



