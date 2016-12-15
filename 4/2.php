<?php

// from http://php.net/manual/en/function.str-rot13.php
function str_rot($s, $n = 13) {
	static $letters = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz';
	$n = (int)$n % 26;
	if (!$n) return $s;
	if ($n < 0) $n += 26;
	if ($n == 13) return str_rot13($s);
	$rep = substr($letters, $n * 2) . substr($letters, 0, $n * 2);
	return strtr($s, $letters, $rep);
}

$fileArray = file('input');
$wordLength = 5;

foreach ($fileArray as $line)
{
	$line = trim($line);

	$matches = array();
	preg_match('/([a-z\-]{1,})(\d+)\[([a-z]{5})\]/', $line, $matches);

	$encWord = str_replace('-', ' ', $matches[1]);
	$letters = str_replace('-', '', $matches[1]);
	$lettersArray = str_split($letters);
	$lettersArray = array_count_values($lettersArray);
	arsort($lettersArray);

	$zone = $matches[2];
	$top = $matches[3];

	$score = array();

	foreach ($lettersArray as $letter => $count)
	{
		if (!array_key_exists($count, $score))
		{
			$score[$count] = '';
		}

		$score[$count] .= $letter;
	}

	$word = '';

	foreach ($score as $count => $letters)
	{
		$length = strlen($word);

		if ($length < 5)
		{
			$sorted = str_split($letters);
			sort($sorted);

			if (count($sorted) < ($wordLength - $length))
			{
				foreach ($sorted as $letter)
				{
					$word .= $letter;
				}
			}
			else
			{
				$i = 0;

				while (strlen($word) < $wordLength)
				{
					$word .= $sorted[$i];
					$i++;
				}
			}
		}
		else
		{
			break;
		}
	}

	if ($word == $top)
	{
		print "$zone - " . str_rot($encWord, $zone) . "\n";
	}
}


?>