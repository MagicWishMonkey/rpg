
// MD5 md5.hash()
var md5=function(){return{hash:function(n){function r(n,r){var t=n[0],c=n[1],i=n[2],a=n[3];t=u(t,c,i,a,r[0],7,-680876936),a=u(a,t,c,i,r[1],12,-389564586),i=u(i,a,t,c,r[2],17,606105819),c=u(c,i,a,t,r[3],22,-1044525330),t=u(t,c,i,a,r[4],7,-176418897),a=u(a,t,c,i,r[5],12,1200080426),i=u(i,a,t,c,r[6],17,-1473231341),c=u(c,i,a,t,r[7],22,-45705983),t=u(t,c,i,a,r[8],7,1770035416),a=u(a,t,c,i,r[9],12,-1958414417),i=u(i,a,t,c,r[10],17,-42063),c=u(c,i,a,t,r[11],22,-1990404162),t=u(t,c,i,a,r[12],7,1804603682),a=u(a,t,c,i,r[13],12,-40341101),i=u(i,a,t,c,r[14],17,-1502002290),c=u(c,i,a,t,r[15],22,1236535329),t=o(t,c,i,a,r[1],5,-165796510),a=o(a,t,c,i,r[6],9,-1069501632),i=o(i,a,t,c,r[11],14,643717713),c=o(c,i,a,t,r[0],20,-373897302),t=o(t,c,i,a,r[5],5,-701558691),a=o(a,t,c,i,r[10],9,38016083),i=o(i,a,t,c,r[15],14,-660478335),c=o(c,i,a,t,r[4],20,-405537848),t=o(t,c,i,a,r[9],5,568446438),a=o(a,t,c,i,r[14],9,-1019803690),i=o(i,a,t,c,r[3],14,-187363961),c=o(c,i,a,t,r[8],20,1163531501),t=o(t,c,i,a,r[13],5,-1444681467),a=o(a,t,c,i,r[2],9,-51403784),i=o(i,a,t,c,r[7],14,1735328473),c=o(c,i,a,t,r[12],20,-1926607734),t=e(t,c,i,a,r[5],4,-378558),a=e(a,t,c,i,r[8],11,-2022574463),i=e(i,a,t,c,r[11],16,1839030562),c=e(c,i,a,t,r[14],23,-35309556),t=e(t,c,i,a,r[1],4,-1530992060),a=e(a,t,c,i,r[4],11,1272893353),i=e(i,a,t,c,r[7],16,-155497632),c=e(c,i,a,t,r[10],23,-1094730640),t=e(t,c,i,a,r[13],4,681279174),a=e(a,t,c,i,r[0],11,-358537222),i=e(i,a,t,c,r[3],16,-722521979),c=e(c,i,a,t,r[6],23,76029189),t=e(t,c,i,a,r[9],4,-640364487),a=e(a,t,c,i,r[12],11,-421815835),i=e(i,a,t,c,r[15],16,530742520),c=e(c,i,a,t,r[2],23,-995338651),t=f(t,c,i,a,r[0],6,-198630844),a=f(a,t,c,i,r[7],10,1126891415),i=f(i,a,t,c,r[14],15,-1416354905),c=f(c,i,a,t,r[5],21,-57434055),t=f(t,c,i,a,r[12],6,1700485571),a=f(a,t,c,i,r[3],10,-1894986606),i=f(i,a,t,c,r[10],15,-1051523),c=f(c,i,a,t,r[1],21,-2054922799),t=f(t,c,i,a,r[8],6,1873313359),a=f(a,t,c,i,r[15],10,-30611744),i=f(i,a,t,c,r[6],15,-1560198380),c=f(c,i,a,t,r[13],21,1309151649),t=f(t,c,i,a,r[4],6,-145523070),a=f(a,t,c,i,r[11],10,-1120210379),i=f(i,a,t,c,r[2],15,718787259),c=f(c,i,a,t,r[9],21,-343485551),n[0]=v(t,n[0]),n[1]=v(c,n[1]),n[2]=v(i,n[2]),n[3]=v(a,n[3])}function t(n,r,t,u,o,e){return r=v(v(r,n),v(u,e)),v(r<<o|r>>>32-o,t)}function u(n,r,u,o,e,f,c){return t(r&u|~r&o,n,r,e,f,c)}function o(n,r,u,o,e,f,c){return t(r&o|u&~o,n,r,e,f,c)}function e(n,r,u,o,e,f,c){return t(r^u^o,n,r,e,f,c)}function f(n,r,u,o,e,f,c){return t(u^(r|~o),n,r,e,f,c)}function c(n){txt="";var t,u=n.length,o=[1732584193,-271733879,-1732584194,271733878];for(t=64;t<=n.length;t+=64)r(o,i(n.substring(t-64,t)));n=n.substring(t-64);var e=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0];for(t=0;t<n.length;t++)e[t>>2]|=n.charCodeAt(t)<<(t%4<<3);if(e[t>>2]|=128<<(t%4<<3),t>55)for(r(o,e),t=0;16>t;t++)e[t]=0;return e[14]=8*u,r(o,e),o}function i(n){var r,t=[];for(r=0;64>r;r+=4)t[r>>2]=n.charCodeAt(r)+(n.charCodeAt(r+1)<<8)+(n.charCodeAt(r+2)<<16)+(n.charCodeAt(r+3)<<24);return t}function a(n){for(var r="",t=0;4>t;t++)r+=d[n>>8*t+4&15]+d[n>>8*t&15];return r}function h(n){for(var r=0;r<n.length;r++)n[r]=a(n[r]);return n.join("")}function v(n,r){return n+r&4294967295}var d="0123456789abcdef".split("");return h(c(n))}}}();

// BASE64 Encoder/Decoder b64.encode()/b64.decode()
var b64=function(){return{encode:function(r){var e,o,t,n,a,d,h,C="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=",c="",f=0;for(r=b64.utf8_encode(r);f<r.length;)e=r.charCodeAt(f++),o=r.charCodeAt(f++),t=r.charCodeAt(f++),n=e>>2,a=(3&e)<<4|o>>4,d=(15&o)<<2|t>>6,h=63&t,isNaN(o)?d=h=64:isNaN(t)&&(h=64),c=c+C.charAt(n)+C.charAt(a)+C.charAt(d)+C.charAt(h);return c},decode:function(r){var e,o,t,n,a,d,h,C="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=",c="",f=0;for(r=r.replace(/[^A-Za-z0-9\+\/\=]/g,"");f<r.length;)n=C.indexOf(r.charAt(f++)),a=C.indexOf(r.charAt(f++)),d=C.indexOf(r.charAt(f++)),h=C.indexOf(r.charAt(f++)),e=n<<2|a>>4,o=(15&a)<<4|d>>2,t=(3&d)<<6|h,c+=String.fromCharCode(e),64!=d&&(c+=String.fromCharCode(o)),64!=h&&(c+=String.fromCharCode(t));return c=b64.utf8_decode(c)},utf8_encode:function(r){r=r.replace(/\r\n/g,"\n");for(var e="",o=0;o<r.length;o++){var t=r.charCodeAt(o);128>t?e+=String.fromCharCode(t):t>127&&2048>t?(e+=String.fromCharCode(t>>6|192),e+=String.fromCharCode(63&t|128)):(e+=String.fromCharCode(t>>12|224),e+=String.fromCharCode(t>>6&63|128),e+=String.fromCharCode(63&t|128))}return e},utf8_decode:function(r){for(var e="",o=0,t=0,n=0;o<r.length;)t=r.charCodeAt(o),128>t?(e+=String.fromCharCode(t),o++):t>191&&224>t?(n=r.charCodeAt(o+1),e+=String.fromCharCode((31&t)<<6|63&n),o+=2):(n=r.charCodeAt(o+1),c3=r.charCodeAt(o+2),e+=String.fromCharCode((15&t)<<12|(63&n)<<6|63&c3),o+=3);return e}}}();