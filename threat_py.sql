-- phpMyAdmin SQL Dump
-- version 4.8.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 23 Agu 2021 pada 15.28
-- Versi server: 10.1.32-MariaDB
-- Versi PHP: 7.2.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `threat_py`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `push_traffic`
--

CREATE TABLE `push_traffic` (
  `no` int(3) NOT NULL,
  `host` varchar(20) DEFAULT NULL,
  `port` varchar(5) DEFAULT NULL,
  `jam_mulai` varchar(8) DEFAULT NULL,
  `jam_selesai` varchar(8) DEFAULT NULL,
  `pesan` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `push_traffic`
--

INSERT INTO `push_traffic` (`no`, `host`, `port`, `jam_mulai`, `jam_selesai`, `pesan`) VALUES
(3, '172.64.195.24', '80', '19', '20', 'looping traffic');

-- --------------------------------------------------------

--
-- Struktur dari tabel `wmi_data`
--

CREATE TABLE `wmi_data` (
  `no` int(4) NOT NULL,
  `ip` varchar(15) DEFAULT NULL,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `wmi_data`
--

INSERT INTO `wmi_data` (`no`, `ip`, `username`, `password`) VALUES
(19, '192.168.88.100', 'administrator', 'passsdsdsdsds'),
(20, '192.168.88.101', 'adi', 'adi');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `push_traffic`
--
ALTER TABLE `push_traffic`
  ADD PRIMARY KEY (`no`);

--
-- Indeks untuk tabel `wmi_data`
--
ALTER TABLE `wmi_data`
  ADD PRIMARY KEY (`no`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `push_traffic`
--
ALTER TABLE `push_traffic`
  MODIFY `no` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT untuk tabel `wmi_data`
--
ALTER TABLE `wmi_data`
  MODIFY `no` int(4) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
