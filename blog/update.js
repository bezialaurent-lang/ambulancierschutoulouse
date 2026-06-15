const fs = require('fs');
const path = require('path');

let content = fs.readFileSync('index.html', 'utf8');

// 1. Swap Jour 22 and Jour 23
const j22Start = content.indexOf('<!-- Jour 22 -->');
const j23Start = content.indexOf('<!-- Jour 23 -->');
const j18Start = content.indexOf('<!-- Jour 18 -->');

if (j22Start !== -1 && j23Start !== -1 && j18Start !== -1) {
    const j22Block = content.substring(j22Start, j23Start);
    const j23Block = content.substring(j23Start, j18Start);
    
    content = content.substring(0, j22Start) + j23Block + j22Block + content.substring(j18Start);
}

// 2. Update Jour 16
const dir16 = path.join(__dirname, 'photos', 'day16');
const files = fs.readdirSync(dir16);
const imageFiles = files.filter(f => {
    const ext = path.extname(f).toLowerCase();
    return !f.endsWith('.mp4') && !f.endsWith('.webm') && !f.endsWith('.mov') && ext !== '.txt' && f !== 'dummy.txt';
});

let newJ16Slides = '';
for (const file of imageFiles) {
    newJ16Slides += `                        <div class="carousel-slide"><img src="photos/day16/${file}" alt="Jour 16"></div>\n`;
}

const j16Regex = /(<div class="carousel-track" id="track-j16">\s*)[\s\S]*?(\s*<\/div>\s*<div class="carousel-controls">)/;
content = content.replace(j16Regex, `$1${newJ16Slides}$2`);

// 3. Remove all video carousel slides
// It matches lines starting with optional spaces, <div class="carousel-slide"><video, spanning multiple lines until </video></div> and optional newline
const videoRegex = /^[ \t]*<div class="carousel-slide"><video[\s\S]*?<\/video><\/div>[ \t]*\r?\n/gm;
content = content.replace(videoRegex, '');

fs.writeFileSync('index.html', content, 'utf8');
console.log("Update successful.");
