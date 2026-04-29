// Auto-dismiss messages after 4 seconds
document.addEventListener('DOMContentLoaded', function () {
  const messages = document.querySelectorAll('.message');
  messages.forEach(function (msg) {
    setTimeout(function () {
      msg.style.transition = 'opacity 0.5s';
      msg.style.opacity = '0';
      setTimeout(function () { msg.remove(); }, 500);
    }, 4000);
  });
});
