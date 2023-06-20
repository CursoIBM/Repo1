//Break
/*
let text = "";

for (let i = 0; i < 10; i++) {
  if (i === 5) break;
  text += i + "<br>";
}

document.write(text);

*/

var year = 2000;

while (year < 2010) {
  year++;

  if (year == 2005) {
    continue;
  } else {
    document.write(year + "<p></p>");
  }
}


