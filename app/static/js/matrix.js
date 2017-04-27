
/*
     11     �� ��setInterval(draw, 33)�趨ˢ�¼��
     12
     13     �� ��String.fromCharCode(1e2+Math.random()*33)���������ĸ
     14
     15     �� ��ctx.fillStyle=��rgba(0,0,0,.05)��; ctx.fillRect(0,0,width,height); ctx.fillStyle=��#0F0��; ��������opacityΪ0.5�İ�͸����ɫ����
     16
     17     �� ��x = (index * 10)+10;��yPositions[index] = y + 10;˳��ȷ����ʾ��ĸ��λ��
     18
     19     �� ��fillText(text, x, y); ��ָ��λ����ʾһ����ĸ ���ϲ���ѭ�����У��ͻ�������ڿ͵۹�����ƬͷЧ����
     20 */
         $(document).ready(function() {
                //�豸���
                var s = window.screen;
                 var width = q.width = s.width;
                var height = q.height;
                var yPositions = Array(300).join(0).split('');
                 var ctx = q.getContext('2d');
                var draw = function() {
                         ctx.fillStyle = 'rgba(0,0,0,.05)';
                         ctx.fillRect(0, 0, width, height);
                         ctx.fillStyle = 'green';/*������ɫ*/
                         ctx.font = '10pt Georgia';
                         yPositions.map(function(y, index) {
                                 text = String.fromCharCode(1e2 + Math.random() * 330);
                                 x = (index * 10) + 10;
                                 q.getContext('2d').fillText(text, x, y);
                                 if (y > Math.random() * 1e4) {
                                        yPositions[index] = 0;
                                     } else {
                                        yPositions[index] = y + 10;
                                     }
                            });
                     };
                RunMatrix();
               function RunMatrix() {
                        Game_Interval = setInterval(draw,30);
                     }
             });