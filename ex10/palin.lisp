(defun palin(st)
(if (string-equal st (reverse st))
(format t "Palindrome")
(format t "not a palindrome")
)
(values)
)

