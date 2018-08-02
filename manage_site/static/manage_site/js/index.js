$(function () {
  //导航栏的筋斗云代码
  function animate(element, target) {
    clearInterval(element.timeId);
    element.timeId = setInterval(function () {
      var current = element.offsetLeft;
      var step = (target - current) / 10;
      step = step > 0 ? Math.ceil(step) : Math.floor(step);
      current += step;
      element.style.left = current + "px";
      if (current == target) {
        clearInterval(element.timeId);
      }
    }, 20);
  }
  var cloud =  $('#nav-cloud')[0];
  var list = $('.nav-icon');
  for (var i = 0; i < list.length; i++) {
    list[i].onmouseover = mouseoverHandle;
    list[i].onclick = clickHandle;
    list[i].onmouseout = mouseoutHandle;
  }
  function mouseoverHandle() {
    animate(cloud, this.offsetLeft);
  }
  var lastPosition = 130;
  function clickHandle() {//点击
    lastPosition = this.offsetLeft;
  }
  function mouseoutHandle() {//离开
    animate(cloud, lastPosition);
  }

});