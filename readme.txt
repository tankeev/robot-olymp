<VirtualHost *:80>
        ServerAdmin root@robotofest.org
        ServerName robotofest.org
        ServerAlias www.robotofest.org
        DocumentRoot /var/www/robot_olymp
        Alias /static /var/www/robot_olymp/staticfiles
        <Directory /var/www/robot_olymp/staticfiles>
                Require all granted
        </Directory>
        <Directory /var/www/robot_olymp/robot_olymp>
                <Files wsgi.py>
                        Require all granted
                </Files>
        </Directory>
        WSGIDaemonProcess robotofest.org python-path=/var/www/robot_olymp:/var/www/robot_olymp/myprojectenv/lib/pyt
hon2.7/site-packages                                                                                               
        WSGIProcessGroup robotofest.org                                                                            
        WSGIScriptAlias / /var/www/robot_olymp/robot_olymp/wsgi.py                                                 
        ErrorLog /var/www/logs/error.log
        CustomLog /var/www/logs/custom.log combined
</VirtualHost>
~                                                                                                                  
~                                                                                                                  
~                                                                                                                  
"/etc/apache2/sites-available/000-default.conf" 20L, 719C                                        1,1           All 
