I also wrote one... it's simpler but it might not handle PATH like above

    function dotenv
        env -S (cat .env) $argv
    end
