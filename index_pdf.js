const execSync = require('child_process').execSync;

const args = process.argv.slice(2);

let resumeName = "";
if (args.length == 0) {
    console.log('Building CV...');
    resumeName = "resume_cv.pdf";
}
else {
    console.log('Building resume based on the following tags: ' + args.join(", "));
    resumeName = "resume_" + args.join("_") + ".pdf";
}

execSync("python resume_filter.py resume.md " + args.join(" ") + " | pandoc -f markdown -t pdf --pdf-engine wkhtmltopdf -c resume-stylesheet.css -s -o " + resumeName, {stdio:[0, 1, 2]});