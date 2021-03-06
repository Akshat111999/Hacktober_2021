mkdir A/B/D/I/L/M  A/B/E/H/K/M  A/C/G/I/K/M  A/C/F/H/K/M
# Now change group of directory K and L [group1 for L and group2 for K]
cd A/B/D/I
# chgrp new_group_name filename/directory
chgrp group1 L
cd A/B/E/H
chgrp group2 K
# Apply Sticky bit and SGID on directory K
chmod 3775 K 
# Change permissions of directories A,B,C,D,E,F,G for OTHERS (remove read and write permission)
# Move to Desktop
chmod 770 A
cd A
chmod 770 *
cd B
chmod 770 *
cd ..
cd C 
chmod 770 *
