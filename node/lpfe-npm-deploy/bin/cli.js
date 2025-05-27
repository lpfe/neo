#!/usr/bin/env node

const { progrma } = require('commander');

program.action(cmd => console.log('✓ Running!!'));

program.parse(process.argv);
