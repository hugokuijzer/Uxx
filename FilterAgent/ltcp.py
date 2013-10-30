import socket, sys
import struct
from struct import *
from dnslib import DNSRecord
import binascii
import time
import pprint
# import FilterAgent.network
class compiledPacket:
    
    def __init__(self):
        self.ips  = []
        self.tcps = []
        self.dns  = []
        
    def add(self,packettype,packet):
        if packettype == 'IP':
            self.ips.append(packet)
        elif packettype == 'TCP':
            self.tcps.append(packet)
        elif packettype == 'DNS' or packettype == 'UDP':
            self.dns.append(packet)
        else:
            raise error
            
class dataPacket:
    
    '''
    Data class that can be sent to the central
    '''
    def __init__(self,ipVersion,ipHLength,ttl,protocol,sourceAddr,destAddr,sourcePort,destPort,seqNum,Ack):
        self.ipVersion = ipVersion
        self.ipHLength = ipHLength
        self.ttl       = ttl
        self.protocol  = protocol
        self.sourceAddr= sourceAddr
        self.destAddr  = destAddr
        self.sourcePort= sourcePort
        self.destPort  = destPort
        self.seqNum    = seqNum
        self.Ack       = Ack

class udpPacket:
    '''
    UDP stored data
    '''
    def __init__(self,sourcePort,destPort,length,data):
        self.sourcePort = sourcePort
        self.destPort   = destPort
        self.length     = length
        self.data       = data
        
def eth_addr (a) :
	b = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (ord(a[0]) , ord(a[1]) , ord(a[2]), ord(a[3]), ord(a[4]) , ord(a[5]))
	return b

def decode_label(message, offset):
	labels = []
			
	while True:
		length, = struct.unpack_from("!B", message, offset)
		
		if(length & 0xC0) == 0xC0:
			pointer, = struct.unpack_from("!H", message, offset)
			offset += 2
			return labels + decode_label(message, pointer & 0x3FFF),offset
			
		if(length & 0xC0) != 0x00:
			raise StandardError("Unknown labelencoding")
			
		offset += 1
		
		if length == 0:
			return labels, offset
		
		labels.append(*struct.unpack_from("!%ds" % length, offset))
		offset += length

DNS_QUERY_SECTION_FORMAT = struct.Struct("!2H")

def decode_question_section(message, offset, qdcount):
	questions = []
	for _ in range(qdcount):
		qname, offset = decode_label(message, offset)
		
		qtype, qclass = DNS_QUERY_SECTION_FORMAT.unpack_from(message,offset)
		offset += DNS_QUERY_SECTION_FORMAT.size
		print(message)
		question = {"domain_name":qname,
					"query_type":qtype,
					"query_class":qclass}
					
		questions.append(question)
	return questions, offset


DNS_QUERY_MESSAGE_HEADER = struct.Struct("!6H")
	
def decode_dns_message(message):
	
	id, misc,qdcount,ancount,nscount,arcount = DNS_QUERY_MESSAGE_HEADER.unpack_from(message)
	
	qr = (misc & 0x8000) != 0
	opcode = (misc & 0x7800) >> 11
	aa = (misc & 0x0400) != 0
	tc = (misc & 0x200) != 0
	rd = (misc & 0x100) != 0
	ra = (misc & 0x80)  != 0
	z  = (misc & 0x70)  != 0
	rcode = misc & 0xF
	
	offset = DNS_QUERY_MESSAGE_HEADER.size
	questions, offset = decode_question_section(message, offset, qdcount)
	
	result = { "id": id,
			   "is_response": qr,
			   "opcode":opcode,
			   "is_authoritative": aa,
			   "is_truncated":tc,
			   "recursion_desired":rd,
			   "recursion_available":ra,
			   "reserved":z,
			   "response_code":rcode,
			   "question_count":qdcount,
			   "answer_count":ancount,
			   "authority_count":nscount,
			   "additional_count":arcount,
			   "questions": questions}
	return result
			
def sniff(duration=5): 
#create an INET, STREAMing socket
    try:
        s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
    except socket.error as msg:
        print ('Socket could not be created. Error Code : ' + str(msg))
        sys.exit()
     
    cPacket = compiledPacket()
    print(cPacket)
    start = time.time()
    print('start time = '+str(start))
    packet = s.recvfrom(65565)
    # print(binascii.unhexlify(packet[0]))
    # receive a packet
    while True:
        'started!'
        packet = s.recvfrom(65565)
        #packet string from tuple
        packet = packet[0]

        #parse ethernet header
        eth_length = 14
        eth_header = packet[:eth_length]
        eth = unpack('!6s6sH', eth_header)
        eth_protocol = socket.ntohs(eth[2])
        #print('Destination MAC' +eth_addr(packet[0:6])+' Source MAC '+eth_addr(packet[6:12])+' Protocol : '+str(eth_protocol))
        
        if eth_protocol == 8:
            
            ip_header = packet[eth_length:20+eth_length]
             
            #now unpack them :)
            iph = unpack('!BBHHHBBH4s4s' , ip_header)
             
            version_ihl = iph[0]
            version = version_ihl >> 4
            ihl = version_ihl & 0xF
             
            iph_length = ihl * 4
             
            ttl = iph[5]
            protocol = iph[6]
            s_addr = socket.inet_ntoa(iph[8]);
            d_addr = socket.inet_ntoa(iph[9]);
             
            #print ('IP Version : ' + str(version) + ' IP Header Length : ' + str(ihl) + ' TTL : ' + str(ttl) + ' Protocol : ' + str(protocol) + ' Source Address : ' + str(s_addr) + ' Destination Address : ' + str(d_addr))
            #print('\n')
            if protocol == 6: 
                tcp_header = packet[iph_length:iph_length+20]
                 
                #now unpack them :)
                tcph = unpack('!HHLLBBHHH' , tcp_header)
                 
                source_port = tcph[0]
                dest_port = tcph[1]
                sequence = tcph[2]
                acknowledgement = tcph[3]
                doff_reserved = tcph[4]
                tcph_length = doff_reserved >> 4
                 
                #print ('TCP PACKET :::  Source Port : ' + str(source_port) + ' Dest Port : ' + str(dest_port) + ' Sequence Number : ' + str(sequence) + ' Acknowledgement : ' + str(acknowledgement) + ' TCP header length : ' + str(tcph_length))
                 
                h_size = iph_length + tcph_length * 4
                data_size = len(packet) - h_size
                 
                #get data from the packet
                data = str(packet[h_size:])
                packet = dataPacket(str(version),str(ihl),str(ttl),str(protocol),str(s_addr),
                str(d_addr),str(source_port),str(dest_port),str(sequence),str(acknowledgement));
                cPacket.add('TCP', packet)
            if protocol == 17:
                u = iph_length + eth_length
                udph_length = 8
                udph_header = packet[u:u+8]
                udph = unpack('!HHHH',udph_header)				
                sourcePort = udph[0]
                destPort   = udph[1]
                length      = udph[2]
                checksum    = udph[3]
                # print(udph)
                h_size = eth_length + iph_length + udph_length
                data_size = len(packet) - h_size
                print ('UDP PACKET ::: Source Port : ' + str(sourcePort) + ' Dest Port : ' + str(destPort) + ' Length : ' 
                + str(length) + ' Checksum : ' + str(checksum)+' Data size :'+str(data_size))
                #get data from the packet
                data = packet[h_size:]
                # print ('UDP DATA ENCODED\n')
                # print(type(data))
                # print(repr(data))
                
                try:
                    # print(data.decode('ascii'))
                    # d = DNSRecord.parse(binascii.unhexlify(data))
                    # pprint.pprint(d)
                    pprint.pprint(decode_dns_message(packet))
                except UnicodeDecodeError as err:
                    print(err)
                    continue
                except binascii.Error as baerr:
                    print(baerr)
                    continue
                except TypeError as te:
                    print(te)
                    continue
                packet = udpPacket(sourcePort, destPort, length, data)
                cPacket.add('UDP', packet)
            #return packet 
            #print ('Data : ' + data)
    return cPacket
    #     printw

try:
	print('starting sniffer!')
	sniff('0')
except KeyboardInterrupt as ki:
	print('Exiting sniffer!')
	sys.exit()

