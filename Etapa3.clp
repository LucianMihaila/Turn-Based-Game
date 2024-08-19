; (defglobal ?*HPPlayer* = 100)
; (defglobal ?*HPCPU* = 100)
; (defglobal ?*SuperPlayer* = 0)
; (defglobal ?*SuperCPU* = 0)
;(defglobal ?*flagMiscare* = 0)
(defglobal ?*flagHPPlayer* = 0)
(defglobal ?*flagHPCPU* = 0)
(defglobal ?*flagSuperPlayer* = 0)
(defglobal ?*flagSuperCPU* = 0)
(defglobal ?*flagEliminarePlayer* = 0)
(defglobal ?*flagEliminareCPU* = 0)


(deffacts JocLupte
    (miscare-aleasa CPUMove HeavyPunch)
    (miscare-aleasa CPUMove LightPunch)
    (miscare-aleasa CPUMove Block)
    (miscare-aleasa PlayerMove)
)

(deftemplate Player
 (field HP (type NUMBER)(default 100))
 (field Super (type NUMBER) (default 0))
 )
 
(deftemplate CPU
 (field HP (type NUMBER) (default 100))
 (field Super (type NUMBER) (default 0))
)


(defrule DefinireBaza
    (declare (salience 9999))
    =>
    (assert (Player))
    (assert (CPU))
)

(defrule DeschidereFisiere
    (declare (salience 10000))
    =>
    (open Input.txt intrare)
    (open Output.txt iesire "w")
    (assert (faza citire))
)

(defrule CitireFisier
    (declare (salience 2000))
    ?a <- (faza citire)
    =>
    (retract ?a)
    (assert (valoare-citita(readline intrare)))
)

(defrule FinalFisier
    (declare (salience 1001))
    ?a <- (valoare-citita EOF)
    =>
    (retract ?a)
    (assert (faza oprire))
)

(defrule OprireCitire
    (declare (salience -1000))
    ?a <- (faza oprire)
    =>
    (retract ?a)
    (close)
)

(defrule CitireMiscare
    (declare (salience 1000))
    ?a <- (valoare-citita ?v)
    ?b <- (miscare-aleasa PlayerMove)
    =>
    (retract ?a ?b)
    (assert (miscare-aleasa PlayerMove (sym-cat ?v)))    
    (assert (faza citire))
)

(defrule CitireHPPlayer
    (declare (salience 999))
    ?a <- (valoare-citita ?v)
    (test(= ?*flagHPPlayer* 0))
    ?b <- (Player (HP ?val1))
    =>
    (retract ?a ?b)
    (bind ?val1 (eval(sym-cat ?v))) 
    (bind ?*flagHPPlayer* ?val1)
    (assert (faza citire))
    (assert (Player (HP ?val1)))
)

(defrule CitireHPCPU
    (declare (salience 998))
    ?a <- (valoare-citita ?v)
    (test(= ?*flagHPCPU* 0))
    ?b <- (CPU (HP ?val1))
    =>
    (retract ?a ?b)
    (bind ?val1 (eval(sym-cat ?v)))
    (bind ?*flagHPCPU* ?val1)
    (assert (faza citire))
    (assert (CPU (HP ?val1)))
)

(defrule CitireSuperPlayer
    (declare (salience 997))
    ?a <- (valoare-citita ?v)
    (test(= ?*flagSuperPlayer* 0))
    ?b <- (Player (Super ?val1))
    =>
    (retract ?a ?b)
    (bind ?*flagSuperPlayer* 1)
    (bind ?val1 (eval(sym-cat ?v)))     
    (assert (faza citire))
    (assert (Player (HP ?*flagHPPlayer*) (Super ?val1)))
)


(defrule CitireSuperCPU
    (declare (salience 995))
    ?a <- (valoare-citita ?v)
    (test(= ?*flagSuperCPU* 0))
    ?b <- (CPU (Super ?val1))
    =>
    (retract ?a ?b)
    (bind ?*flagSuperCPU* 1)
    (bind ?val1 (eval(sym-cat ?v)))
    (assert (faza citire))
    (assert (CPU (HP ?*flagHPCPU*) (Super ?val1)))
)

; (defrule LimitareSuper
    ; (declare (salience 1001))
    ; (test (> ?*SuperPlayer* 5))
    ; =>
    ; (bind (= ?*SuperPlayer* 5))
; )

(defrule LuptaCPUHeavyPunch
    (miscare-aleasa CPUMove HeavyPunch)
    ?a <- (miscare-aleasa PlayerMove ?v)
    ?b <- (Player (HP ?valHPPlayer) (Super ?valSuperPlayer))
    ?c <- (CPU (HP ?valHPCPU) (Super ?valSuperCPU))
    =>
    (retract ?a ?b ?c)
    (if (eq ?v HeavyPunch)
        then (and(bind ?valHPPlayer (- ?valHPPlayer 7)) (bind ?valHPCPU (- ?valHPCPU 7)))
    )
    (if (eq ?v LightPunch)
        then (and (bind ?valHPCPU (- ?valHPCPU 9)) (bind ?valSuperPlayer (+ ?valSuperPlayer 1)) (bind ?valSuperCPU (+ ?valSuperCPU 0.5)))
    )
    (if (eq ?v Block)
        then (and (bind ?valHPPlayer (- ?valHPPlayer 14)) (bind ?valSuperPlayer (+ ?valSuperPlayer 0.5)) (bind ?valSuperCPU (+ ?valSuperCPU 1)))
    )
    (if (and(eq ?v Super) (>= ?valSuperPlayer 5))
        then (and (bind ?valHPCPU (- ?valHPCPU 33)) (bind ?valSuperPlayer 0))
    )
    (assert (Player (HP ?valHPPlayer) (Super ?valSuperPlayer)))
    (assert (CPU (HP ?valHPCPU) (Super ?valSuperCPU)))
    (printout iesire HeavyPunch crlf)
)

(defrule LuptaCPULightPunch
    (miscare-aleasa CPUMove LightPunch)
    ?a <- (miscare-aleasa PlayerMove ?v)
    ?b <- (Player (HP ?valHPPlayer) (Super ?valSuperPlayer))
    ?c <- (CPU (HP ?valHPCPU) (Super ?valSuperCPU))
    =>
    (retract ?a ?b ?c)
    (if (eq ?v LightPunch)
        then (and(bind ?valHPPlayer (- ?valHPPlayer 4)) (bind ?valHPCPU (- ?valHPCPU 4)))
    )
    (if (eq ?v Block)
        then (and(bind ?valSuperPlayer (+ ?valSuperPlayer 1)) (bind ?valSuperCPU (+ ?valSuperCPU 0.5)))
    )
    (if (eq ?v HeavyPunch)
        then (and (bind ?valHPPlayer (- ?valHPPlayer 7)) (bind ?valSuperPlayer (+ ?valSuperPlayer 0.5)) (bind ?valSuperCPU (+ ?valSuperCPU 1)))
    )
    (if (and(eq ?v Super) (>= ?valSuperPlayer 5))
        then (and (bind ?valHPCPU (- ?valHPCPU 33)) (bind ?valSuperPlayer 0))
    )
    (assert (Player (HP ?valHPPlayer) (Super ?valSuperPlayer)))
    (assert (CPU (HP ?valHPCPU) (Super ?valSuperCPU)))
    (printout iesire LightPunch crlf)
 )
(defrule LuptaCPUBlock
    (miscare-aleasa CPUMove Block)
    ?a <- (miscare-aleasa PlayerMove ?v)
    ?b <- (Player (HP ?valHPPlayer) (Super ?valSuperPlayer))
    ?c <- (CPU (HP ?valHPCPU) (Super ?valSuperCPU))
    =>
    (retract ?a ?b ?c)
    (if (eq ?v Block)
        then (and(bind ?valHPPlayer ?valHPPlayer) (bind ?valHPCPU ?valHPCPU))
    )
    (if (eq ?v HeavyPunch)
        then (bind ?valHPCPU (- ?valHPCPU 14))(bind ?valSuperPlayer (+ ?valSuperPlayer 1)) (bind ?valSuperCPU (+ ?valSuperCPU 0.5))
    )
    (if (eq ?v LightPunch)
        then (and(bind ?valSuperPlayer (+ ?valSuperPlayer 0.5)) (bind ?valSuperCPU (+ ?valSuperCPU 1)))
    )
    (if (and(eq ?v Super) (>= ?valSuperPlayer 5))
        then (and (bind ?valHPCPU (- ?valHPCPU 33)) (bind ?valSuperPlayer 0))
    )
    (assert (Player (HP ?valHPPlayer) (Super ?valSuperPlayer)))
    (assert (CPU (HP ?valHPCPU) (Super ?valSuperCPU)))
    (printout iesire Block crlf)
  )  
(defrule LuptaCPUSuper
    (declare (salience 9001))
    ?a <- (miscare-aleasa PlayerMove ?v)
    ?b <- (Player (HP ?valHPPlayer) (Super ?valSuperPlayer))
    ?c <- (CPU (HP ?valHPCPU) (Super ?valSuperCPU))
    (test (>= ?valSuperCPU 5))
    =>
    (if (and(eq ?v Super) (>= ?valSuperPlayer 5))
        then (and (bind ?valHPCPU ?valHPCPU) (bind ?valHPPlayer ?valHPPlayer) (bind ?valSuperPlayer 0) (bind ?valSuperCPU 0))
    )
    (retract ?a ?b ?c)
    (if (neq ?v Super) 
	then (and(bind ?valHPPlayer (- ?valHPPlayer 33)) (bind ?valSuperCPU 0))
    )
    	(assert (Player (HP ?valHPPlayer) (Super ?valSuperPlayer)))
    	(assert (CPU (HP ?valHPCPU) (Super ?valSuperCPU)))
    	(printout iesire Super crlf)
    )    

(defrule ScriereFisier
    (declare (salience -999))
    (Player (HP ?valHPPlayer) (Super ?valSuperPlayer))
    (CPU (HP ?valHPCPU) (Super ?valSuperCPU))
    =>
    (printout iesire ?valHPPlayer crlf ?valHPCPU crlf ?valSuperPlayer crlf ?valSuperCPU)
)

(defrule DecidereCastigator
    (declare (salience -997))
    (Player (HP ?valHPPlayer) (Super ?valSuperPlayer))
    (CPU (HP ?valHPCPU) (Super ?valSuperCPU))
    =>
    (if (and(<= ?valHPCPU 0) (> ?valHPPlayer 0))
        then (printout iesire "Player Wins" crlf)
    )
    (if (and(<= ?valHPPlayer 0) (> ?valHPCPU 0))
        then (printout iesire "CPU Wins" crlf)
    )
    (if (and (<= ?valHPPlayer 0) (<= ?valHPCPU 0))
        then (printout iesire "Draw" crlf)
    )
)

