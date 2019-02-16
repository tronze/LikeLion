if( /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent) ) {
  var highlight_list = Array.prototype.slice.call(document.querySelectorAll('.highlight-green span'));
  console.log(highlight_list);
  highlight_list.forEach(function(item){
    item.setAttribute('class', 'mobile');
  });
}

var sections = Array.from(document.querySelectorAll('body > section')).slice(1,4);


var findSpan = function(context) {
  var span_list = Array.prototype.slice.call(context.querySelectorAll('.highlight-green span'));
  return span_list;
};
sections.forEach(function(item) {
  item.addEventListener('mouseenter', function() {
    var items = findSpan(this);
    items.forEach(function(item){
      item.setAttribute('class', 'on');
    });
  });
  item.addEventListener('mouseleave', function() {
    var items = findSpan(this);
    items.forEach(function(item){
      item.setAttribute('class', '');
    });
  });
  item.addEventListener('touchstart', function() {
    var items = findSpan(this);
    items.forEach(function(item){
      item.setAttribute('class', 'on');
    });
  });
  item.addEventListener('touchend', function() {
    var items = findSpan(this);
    items.forEach(function(item){
      item.setAttribute('class', '');
    });
  });
});