const images = document.querySelectorAll(".display");
const large_display_container = document.getElementById("large_display_container");
large_display_container.setAttribute("onclick", "hideLarge()");
for (let image of images) {
  let src = image.getAttribute("src");
  image.setAttribute("onclick", `showLarge("${src}")`);
}

function showLarge(src) {
  const large_display_container = document.getElementById("large_display_container");
  const large_display_img = document.getElementById("large_display_img");
  large_display_img.setAttribute("src", src);
  large_display_img.style.opacity = "1";
  large_display_container.style.zIndex = "100";
}

function hideLarge() {
  const large_display_container = document.getElementById("large_display_container");
  const large_display_img = document.getElementById("large_display_img");
  large_display_img.style.opacity = "0";
  large_display_img.setAttribute("src", "");
  large_display_container.style.zIndex = "-1";
}