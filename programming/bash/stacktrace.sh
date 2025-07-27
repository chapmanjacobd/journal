#!/bin/bash

die() {
  local frame=0
  while caller $frame; do
    ((++frame));
  done
  echo "$*"
  exit 1
}

f1() { die "*** an error occured ***"; }
f2() { f1; }
f3() { f2; }

f3
