<?php
$allowed_ip = ['localhost', '127.0.0.1'];
$allowed_user_agent = 'Martin';

// Initialize the allowed variable to false
$allowed = false;

// Check if the incoming request is from an allowed IP address
if (isset($_SERVER['HTTP_X_FORWARDED_FOR']) && in_array($_SERVER['HTTP_X_FORWARDED_FOR'], $allowed_ip)) {
    // Additionally, check if the user agent matches "Martin"
    if (isset($_SERVER['HTTP_USER_AGENT']) && strpos($_SERVER['HTTP_USER_AGENT'], $allowed_user_agent) !== false) {
        $allowed = true; // Set allowed to true only if both conditions are met
    }
}
?>

<!DOCTYPE html>
<html>

<head>
    <title>Agent Martin</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    colors: {
                        primary: {
                            "500": "#3b82f6", // Keeping primary color definition for use
                        }
                    }
                }
            }
        }
    </script>
</head>

<body class="bg-green-200 grid h-screen place-items-center">
    <?php
    if (!$allowed) {
    ?>
        <div class="py-8 px-4 mx-auto max-w-screen-xl text-center">
            <h1 class="mb-4 text-7xl tracking-tight font-extrabold text-primary-500">
                <img src="agent.jpg" alt="Agent Icon" class="mx-auto">
            </h1>
            <p class="mb-4 text-3xl font-bold text-gray-900 text-black"><br><br>
                True agents never share their secrets other than organization members!  
            </p>
        </div>
    <?php
    } else {
    ?>
        <section class="antialiased">
            <div class="max-w-screen-xl px-4 py-8 mx-auto text-center">
                <h2 class="text-4xl font-extrabold leading-tight tracking-tight text-black">
                    Secret: 
                </h2><br>
                <h2 class="text-4xl font-extrabold leading-tight tracking-tight text-black">
                    BUETCTF{0nly_1n5ider5_are_All0w3d_t0_kn0w_ab0ut_th3_53cr3t5}
                </h2>
            </div>
        </section>
    <?php
    }
    ?>
</body>

</html>
