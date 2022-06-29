# wordlistAPI

This is an API to get custom wordlist based on existing ones. You can get shorter wordlist or a custom wordlist by line range. You can also get on word of a list

## Usage

(it will evolve in time)

GET => /rocku/<index> : give you the word at position <index> in rockyou.txt

GET => /rocku/?start=<nb1>&end=<nb2> : give you a custom wordlist from a range between start and end parameters

GET => /rocku/<nb>/lines : give you a custom wordlist from the start to nb line