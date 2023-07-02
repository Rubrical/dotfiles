#!/bin/bash

# General use variables
nc="--noconfirm"

# inicializing: 
printf "Starting installations\n"
Sleep 5
echo "Installaling Yay"
Sleep 5

# Installaling Yay

sudo pacman -S ${nc} --needed git base-devel && git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -si ${nc}
yay -Y --gendb
yay -Syu ${nc} --devel
yay -Y --devel --save
yay -Syu ${nc}

printf "Installaling system programs\n"
Sleep 5

# system programs 
sudo pacman -S ${nc} qtile alacritty kitty starship feh pavucontrol sxhkd rofi volumeicon dunst

printf "Installaling personal programs\n"
Sleep 5

# personal programs
sudo pacman -S ${nc} flameshot notepadqq vlc mvp neovim gparted okular galculator freedownloadmanager telegram-desktop spotify manuskript ristretto 

# fonts
printf "Installaling fonts\n"
Sleep 5

yay -S ${nc} ttf-jetbrains-mono-nerd-font ttf-jetbrains-mono ttf-font-family


# more personal programs
printf "Installaling the aur packeges\n"
Sleep 5

yay -S ${nc} discord brave onlyoffice-documentserver-bin picom-git

# More configuration
printf "Configuring starship\n"
echo eval "$(starship init bash)" >> ~/.bashrc

# configuring aliases
{
    alias ls="ls -a --color=auto";
    alias update="sudo pacman -Syyuu";
    alias vim=nvim;            
} >> ~/.bashrc

Sleep 5

# cloning files from github
printf "Putting it all together\n"
Sleep 5

cd ~/Downloads/ && git clone https://github.com/Rubrical/dotfiles.git && cd dotfiles/.config && mv -b qtile/ picom/ rofi/ sxhdk/ neofetch/ nvim/ starship.toml ~/.config_sex
rm -rf ~Downloads/dotfiles

# Installing archlinux logout and betterlockscreen
cd ~/Downloads && git clone https://github.com/arcolinux/archlinux-logout.git
cd ~/Downloads/archlinux-logout/etc && mv -b archlinux-logout.conf /etc
cd ~/Downloads/archlinux-logout/usr/bin && mv -b archlinux-betterlockscreen archlinux-logout /usr/bin
cd ~/Downlodas/archlinux-logout/usr/share && mv -b archlinux-betterlockscreen/ archlinux-logout/ archlinux-logout-themes/ icons/hicolor/scalable/apps /usr/share/
cd ~/Downlodas/archlinux-logout/usr/share/applications && mv -b archlinux-betterlockscreen.desktop /usr/share/applications/

printf "Please reboot to save changes\n"
Sleep 2
read -r "Do you wish to reboot the computer? (Y/n) " choice
case "$choice" in
    y|Y|"" ) sudo reboot;;
    * ) echo "Reboot to make changes persirst";;
esac
