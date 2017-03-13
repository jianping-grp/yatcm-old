#!/bin/sh
NAME="yatcm"                                  # Name of the application
DJANGODIR=/www/yatcm             # Django project directory
USER=jianping_grp                                        # the user to run as
GROUP=webapps                                     # the group to run as
NUM_WORKERS=11                                     # how many worker processes should Gunicorn spawn
ADDRESS=0.0.0.0:8012
DJANGO_SETTINGS_MODULE=yatcm.settings             # which settings file should Django use
DJANGO_WSGI_MODULE=yatcm.wsgi  
LOGFILE=/www/jianping_grp/logs/yatcm.log
LOGDIR=$(dirname $LOGFILE)
echo "Starting $NAME as `whoami`"
 
# Activate the virtual environment
#cd $DJANGODIR
#. /home/jiohua/virtualenvs/mezzanine/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:/www:$PYTHONPATH
. /home/jiohua/virtualenvs/yatcm/bin/activate 
# Create the run directory if it doesn't exist

test -d $LOGDIR || mkdir -p $LOGDIR
# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec  /home/jiohua/virtualenvs/yatcm/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --log-level=debug \
  --log-file=$LOGFILE -b $ADDRESS >> $LOGFILE













