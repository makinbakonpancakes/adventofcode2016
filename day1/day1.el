(defun read-lines (filePath)
  "Return a list of lines of a file at filePath."
  (with-temp-buffer
    (insert-file-contents filePath)
    (split-string (buffer-string) "\n" t)))

(defun get-moves-list (moves)
  (mapcar (lambda (x) (split-string x ", " t))
          (read-lines "./input.txt")))

(defun turn-right (direction)
  (if (string= direction "n") "e"
    (if (string= direction "e") "s"
      (if (string= direction "s") "w"
        (if (string= direction "w") "n")))))

(defun problem ()
  (interactive "")
  (let ((pos (0 0))
        (direction (0 1))
        (visited)
        (turns (get-moves-list)))
    (while turns
      (let ((move (car turns))
            (turn (car (split-string move "" t)))
            (distance (cdr (split-string move "" t))))
        (if (eq (turn "L"))
            (setq direction (* #C(0 1) direction))
          (setq direction (* #C(0 -1) direction))
          (while (/= distance 0)
            (setq pos (+ pos direction))
            (add-to-list 'visited pos)
      (if 
      (cdr turns))
  ))

(display (problem))
