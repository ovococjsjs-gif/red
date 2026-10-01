const fs = require('fs');
const { Resvg } = require('/home/user/.tools/node_modules/@resvg/resvg-js');
const svg = fs.readFileSync('pelican_on_bicycle.svg', 'utf8');
const r = new Resvg(svg, { fitTo: { mode: 'width', value: 1000 }, background: 'rgba(255,255,255,0)' });
fs.writeFileSync('pelican_on_bicycle.png', r.render().asPng());
console.log('png written');
