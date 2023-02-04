{ pkgs }: {
    deps = [
        pkgs.sudo
        pkgs.busybox
        pkgs.jq.bin
        pkgs.bashInteractive
        pkgs.man
    ];
}