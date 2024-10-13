You can also read xlsx if you have nushell installed. This works on both Linux and Windows:

.gitconfig

    [diff "excel"]
        textconv = nu ~/bin/excel2csv.nu
        cachetextconv = true
        binary = true

.gitattributes

    *.xlsx binary diff=excel

excel2csv.nu

    def main [path: string] {
        open $path | transpose k v | each { |row|
            let sheet_name = $row.k
            let sheet_data = $row.v
    
            $"($sheet_name) " + ($sheet_data | headers | to csv)
        } | to text
    }
