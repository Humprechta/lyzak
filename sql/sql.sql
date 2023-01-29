-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Počítač: 127.0.0.1
-- Vytvořeno: Ned 29. led 2023, 14:59
-- Verze serveru: 10.4.22-MariaDB
-- Verze PHP: 7.4.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Databáze: `python_projects`
--

use python_projects;

-- --------------------------------------------------------

--
-- Struktura tabulky `objednavka`
--

CREATE TABLE `objednavka` (
  `id` int(11) NOT NULL,
  `id_user` int(11) DEFAULT NULL,
  `id_bota` int(11) DEFAULT NULL,
  `id_platba` int(11) DEFAULT NULL,
  `vytvoreni` date NOT NULL,
  `kusu` int(11) NOT NULL,
  `zaplaceno` tinyint(1) NOT NULL,
  `dodano` date DEFAULT NULL
) ;

-- --------------------------------------------------------

--
-- Struktura tabulky `platba`
--

CREATE TABLE `platba` (
  `id` int(11) NOT NULL,
  `nazev` varchar(49) NOT NULL,
  `cena` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Vypisuji data pro tabulku `platba`
--

INSERT INTO `platba` (`id`, `nazev`, `cena`) VALUES
(1, 'dobirka', 90),
(2, 'na prodejne', 0);

-- --------------------------------------------------------

--
-- Struktura tabulky `produkt_bota`
--

CREATE TABLE `produkt_bota` (
  `id` int(11) NOT NULL,
  `id_znacka` int(11) DEFAULT NULL,
  `nazev` varchar(20) NOT NULL,
  `cena` float NOT NULL,
  `velikost` enum('35','36','37','38','39','40','41','42','43','44','45') DEFAULT NULL,
  `kus` int(11) DEFAULT NULL
) ;

--
-- Vypisuji data pro tabulku `produkt_bota`
--

INSERT INTO `produkt_bota` (`id`, `id_znacka`, `nazev`, `cena`, `velikost`, `kus`) VALUES
(40, 1, 'NIKE++', 2025, '35', 10),
(41, 1, 'NIKE++', 2025, '38', 9);

-- --------------------------------------------------------

--
-- Struktura tabulky `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `jmeno` varchar(20) NOT NULL,
  `prijmeni` varchar(20) DEFAULT NULL,
  `user_name` varchar(49) DEFAULT NULL,
  `user_password` varchar(49) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Vypisuji data pro tabulku `user`
--

INSERT INTO `user` (`id`, `jmeno`, `prijmeni`, `user_name`, `user_password`) VALUES
(1, 'Pepa', 'Pepovic', 'pepa00', '44c5590f38f774f883e01500207a9dc81eae9468'),
(2, 'Karel', 'Karlovic', 'karel00', 'c5ea6cc0551f0eff323a6a1fdffa36e112f54041');

-- --------------------------------------------------------

--
-- Struktura tabulky `znacka`
--

CREATE TABLE `znacka` (
  `id` int(11) NOT NULL,
  `nazev` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Vypisuji data pro tabulku `znacka`
--

INSERT INTO `znacka` (`id`, `nazev`) VALUES
(1, 'adiddas'),
(2, 'nike'),
(3, 'Armani');

--
-- Indexy pro exportované tabulky
--

--
-- Indexy pro tabulku `objednavka`
--
ALTER TABLE `objednavka`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_user` (`id_user`),
  ADD KEY `id_bota` (`id_bota`),
  ADD KEY `id_platba` (`id_platba`);

--
-- Indexy pro tabulku `platba`
--
ALTER TABLE `platba`
  ADD PRIMARY KEY (`id`);

--
-- Indexy pro tabulku `produkt_bota`
--
ALTER TABLE `produkt_bota`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_znacka` (`id_znacka`);

--
-- Indexy pro tabulku `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- Indexy pro tabulku `znacka`
--
ALTER TABLE `znacka`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT pro tabulky
--

--
-- AUTO_INCREMENT pro tabulku `objednavka`
--
ALTER TABLE `objednavka`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pro tabulku `platba`
--
ALTER TABLE `platba`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT pro tabulku `produkt_bota`
--
ALTER TABLE `produkt_bota`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pro tabulku `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT pro tabulku `znacka`
--
ALTER TABLE `znacka`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- Omezení pro exportované tabulky
--

--
-- Omezení pro tabulku `objednavka`
--
ALTER TABLE `objednavka`
  ADD CONSTRAINT `objednavka_ibfk_1` FOREIGN KEY (`id_user`) REFERENCES `user` (`id`),
  ADD CONSTRAINT `objednavka_ibfk_2` FOREIGN KEY (`id_bota`) REFERENCES `produkt_bota` (`id`),
  ADD CONSTRAINT `objednavka_ibfk_3` FOREIGN KEY (`id_platba`) REFERENCES `platba` (`id`);

--
-- Omezení pro tabulku `produkt_bota`
--
ALTER TABLE `produkt_bota`
  ADD CONSTRAINT `produkt_bota_ibfk_1` FOREIGN KEY (`id_znacka`) REFERENCES `znacka` (`id`);
COMMIT;

create view select_bota as
	select produkt_bota.id as id,znacka.nazev as znacka,produkt_bota.nazev as nazev,velikost,kus,cena from produkt_bota inner join znacka on znacka.id = id_znacka;


create view select_objednavka as
	select produkt_bota.nazev as nazev, produkt_bota.cena as cena, velikost, kusu, zaplaceno, dodano, vytvoreni, platba.nazev as platba from objednavka inner join produkt_bota on produkt_bota.id = id_bota inner join platba on platba.id = id_platba;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
