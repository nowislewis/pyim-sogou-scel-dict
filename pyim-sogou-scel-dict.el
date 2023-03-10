;;; License:

;; This file is not part of GNU Emacs.

;; This program is free software; you can redistribute it and/or
;; modify it under the terms of the GNU General Public License
;; as published by the Free Software Foundation; either version 3
;; of the License, or (at your option) any later version.

;; This program is distributed in the hope that it will be useful,
;; but WITHOUT ANY WARRANTY; without even the implied warranty of
;; MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
;; GNU General Public License for more details.

;; You should have received a copy of the GNU General Public License
;; along with GNU Emacs; see the file COPYING.  If not, write to the
;; Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
;; Boston, MA 02110-1301, USA.

;;; Commentary:

;;; Code:
(require 'pyim-dict)

;;;###autoload
(defun pyim-sogou-scel-dict-enable ()
  "Add sogou scel dict to pyim."
  (interactive)
  (let* ((dir (file-name-directory
               (locate-library "pyim-sogou-scel-dict.el")))
         (file (concat dir "pyim-sogou-scel-dict.pyim")))
    (when (file-exists-p file)
      (if (featurep 'pyim-dict)
          (pyim-extra-dicts-add-dict
           `(:name "pyim-sogou-scel-dict" :file ,file :elpa t))
        (message "pyim 没有安装，pyim-sogou-scel-dict 启用失败。")))))

(provide 'pyim-sogou-scel-dict)

;;
;;; pyim-pyim-sogou-scel-dict.el ends here
