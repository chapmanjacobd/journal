I also have this from time to time on 8845H w/ Radeon 780M. I'm able to reset to login by SSH'ing in and running `reset-amdgpu`:

    function reset-amdgpu
        echo 1 | sudo tee /sys/class/drm/card0/device/remove
        echo 1 | sudo tee /sys/class/drm/card1/device/remove
        echo 1 | sudo tee /sys/bus/pci/rescan
    end

But this closes everything that is open... 

I also use KDE. Do you use Kitty by any chance? I feel like it might be related. I've noticed that it only freezes when Kitty is open--but this may also just be coincidence
